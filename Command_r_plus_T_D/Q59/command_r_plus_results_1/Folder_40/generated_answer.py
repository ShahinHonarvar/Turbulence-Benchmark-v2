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
        for num in range(limit, 1, -1):
            if str(num).count('0') > 0:
                continue
            is_prime_num = True
            temp = num
            while temp > 0:
                temp //= 10
                if not is_prime(num):
                    is_prime_num = False
                    break
            if is_prime_num:
                primes.append(num)
        return primes
    limit = numbers[10]
    return sorted(generate_left_truncatable_primes(limit), reverse=True)