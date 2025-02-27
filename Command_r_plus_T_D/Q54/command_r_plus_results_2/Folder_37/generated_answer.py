def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(limit):
        primes = []
        for i in range(1, 10):
            num = i
            while num < limit:
                if is_prime(num):
                    primes.append(num)
                num = num * 10 + i
        return primes
    x = numbers[35]
    right_truncatable_primes = generate_right_truncatable_primes(x)
    right_truncatable_primes.sort(reverse=True)
    return [i for i in right_truncatable_primes if i < x]