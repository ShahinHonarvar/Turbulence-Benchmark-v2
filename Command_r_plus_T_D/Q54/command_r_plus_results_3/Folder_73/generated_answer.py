def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generate_right_truncatable_primes(n: int) -> list[int]:
        primes = []
        for i in range(1, 10):
            num = n * 10 + i
            if is_prime(num):
                primes.append(num)
        return primes
    primes = []
    for num in range(1, numbers[97]):
        if is_prime(num):
            right_truncatable_primes = [num]
            temp = num
            while len(str(temp)) > 1:
                temp //= 10
                right_truncatable_primes.extend(generate_right_truncatable_primes(temp))
            primes.extend(set(right_truncatable_primes))
    return sorted(primes)