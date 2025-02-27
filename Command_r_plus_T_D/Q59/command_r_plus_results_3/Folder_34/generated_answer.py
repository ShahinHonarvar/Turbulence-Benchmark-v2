def all_left_truncatable_prime(limit_tup: tuple[int, ...]) -> list[int]:

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
            if new_num in [0, 1, 2, 3, 5, 7, 9] and is_prime(new_num) and is_prime(int(str(num)[1:])):
                left_truncatable_primes.extend(generate_left_truncatable_primes(new_num))
        return left_truncatable_primes
    limit = limit_tup[18]
    left_truncatable_primes = []
    for num in range(2, limit):
        left_truncatable_primes.extend(generate_left_truncatable_primes(num))
    return sorted(set(left_truncatable_primes), reverse=True)