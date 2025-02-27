def all_left_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_left_truncatable_primes(limit: int) -> list[int]:
        primes = []
        for num in range(2, limit + 1):
            if is_prime(num):
                str_num = str(num)
                left_truncate = True
                for i in range(1, len(str_num)):
                    if not is_prime(int(str_num[:i])) or str_num[0] == '0':
                        left_truncate = False
                        break
                if left_truncate:
                    primes.append(num)
        return primes
    limit = numbers[61]
    left_truncatable_primes = generate_left_truncatable_primes(limit)
    return sorted(left_truncatable_primes)