def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[466]
    pixels = sorted({2, 3, 5, 7})
    left_truncatable_primes = []
    while True:
        for i in range(len(pixels) - 1, -1, -1):
            for j in range(10):
                n = pixels[i] * 10 + j
                if n < x and is_prime(n):
                    pixels.append(n)
        if pixels[-1] >= x:
            break
    return sorted(left_truncatable_primes, reverse=True)