def all_left_truncatable_prime(input_tuple: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_left_truncatable_primes(limit: int) -> list[int]:
        primes = []
        for num in range(limit, 1, -1):
            if str(num).count('0') > 0 or not is_prime(num):
                continue
            temp = num
            while temp > 0:
                temp //= 10
                if temp > 0 and (not is_prime(temp)):
                    break
            if temp == 0:
                primes.append(num)
        return primes
    limit = input_tuple[0]
    left_truncatable_primes = generate_left_truncatable_primes(limit)
    return sorted(left_truncatable_primes, reverse=True)