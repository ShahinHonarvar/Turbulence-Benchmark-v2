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
        for i in range(2, limit):
            if is_prime(i):
                left_truncations = [i]
                num = i
                while len(str(num)) > 1:
                    num //= 10
                    if is_prime(num):
                        left_truncations.append(num)
                    else:
                        break
                if len(left_truncations) == len(str(i)):
                    primes.append(i)
        return primes
    limit = numbers[41]
    left_truncatable_primes = generate_left_truncatable_primes(limit)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes