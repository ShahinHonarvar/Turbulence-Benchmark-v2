def all_right_truncatable_prime(input_tuple: tuple[int]) -> list[int]:

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
                truncated_num = num // 10
                while truncated_num != 0:
                    if not is_prime(truncated_num):
                        break
                    truncated_num //= 10
                else:
                    primes.append(num)
        return primes
    x = input_tuple[0]
    right_truncatable_primes = generate_right_truncatable_primes(x)
    return sorted(right_truncatable_primes, reverse=True)