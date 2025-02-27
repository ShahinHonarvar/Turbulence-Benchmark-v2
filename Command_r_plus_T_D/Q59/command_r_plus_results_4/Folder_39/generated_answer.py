def all_left_truncatable_prime(limit: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_left_truncatable_primes(num: int) -> list[int]:
        if num < 10 and is_prime(num):
            return [num]
        left_truncatable_primes = []
        for i in range(1, num // 10 + 1):
            new_num = num - i * 10 ** (len(str(num)) - 1)
            if new_num > 0 and is_prime(new_num) and (str(new_num)[0] != '0'):
                left_truncatable = generate_left_truncatable_primes(new_num)
                if left_truncatable:
                    left_truncatable_primes.extend(left_truncatable)
        return left_truncatable_primes
    left_truncatable_primes = []
    for num in range(2, limit[30]):
        if is_prime(num):
            left_truncatable = generate_left_truncatable_primes(num)
            if left_truncatable:
                left_truncatable_primes.extend(left_truncatable)
    return sorted(set(left_truncatable_primes), reverse=True)