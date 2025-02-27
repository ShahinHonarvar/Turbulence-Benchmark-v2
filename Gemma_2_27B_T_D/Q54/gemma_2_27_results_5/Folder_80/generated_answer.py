def all_right_truncatable_prime(numbers):
    x = numbers[14]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x - 1, 1, -1):
        n = i
        is_truncatable = True
        while n > 0:
            if not is_prime(n):
                is_truncatable = False
                break
            n //= 10
        if is_truncatable:
            primes.append(i)
    primes.sort(reverse=True)
    return primes