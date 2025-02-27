def all_right_truncatable_prime(n):

    def is_prime(num):
        if num in (0, 1):
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_rtp(num):
        temp = num
        while temp:
            if not is_prime(temp):
                return False
            temp //= 10
        return True
    primes = [i for i in reversed(range(1, n[81])) if is_prime(i) and is_rtp(i)]
    return sorted(primes, reverse=True)