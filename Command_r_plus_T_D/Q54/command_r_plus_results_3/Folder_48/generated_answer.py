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
        for num in range(1, limit):
            if is_prime(num):
                right_truncatable = True
                temp_num = num
                while temp_num > 0:
                    temp_num //= 10
                    if not is_prime(num - temp_num * 10):
                        right_truncatable = False
                        break
                if right_truncatable:
                    primes.append(num)
        return primes
    x = numbers[835]
    return generate_right_truncatable_primes(x)