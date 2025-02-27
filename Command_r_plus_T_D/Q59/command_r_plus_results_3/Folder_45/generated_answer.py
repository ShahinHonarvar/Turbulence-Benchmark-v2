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
        for i in range(1, num):
            truncated_num = num // 10 ** i * 10
            if str(truncated_num).endswith('0'):
                continue
            if is_prime(truncated_num) and is_prime(num):
                left_truncatable_primes.extend(generate_left_truncatable_primes(truncated_num))
        return left_truncatable_primes
    left_truncatable_primes = []
    for num in range(2, limit[61]):
        left_truncatable_primes.extend(generate_left_truncatable_primes(num))
    return sorted(set(left_truncatable_primes))