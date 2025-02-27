def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(limit: int) -> list[int]:
        primes = []
        for num in range(limit, 0, -1):
            if is_prime(num):
                temp_num = num
                while temp_num > 0:
                    temp_num //= 10
                    if is_prime(num - temp_num):
                        primes.append(num)
                        break
        return primes
    limit = numbers[39]
    right_truncatable_primes = generate_right_truncatable_primes(limit)
    return sorted(right_truncatable_primes)