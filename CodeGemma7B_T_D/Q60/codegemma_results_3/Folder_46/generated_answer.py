def all_left_right_truncatable_prime(a):
    b = a[33]

    def prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable_prime(n):
        if n < 2 or '0' in str(n) or (not prime(n)):
            return False
        while n >= 10:
            n = int(str(n)[1:])
            if not prime(n):
                return False
        return True

    def right_truncatable_prime(n):
        if n < 10 or '0' in str(n) or (not prime(n)):
            return False
        while n > 9:
            n = int(str(n)[:-1])
            if not prime(n):
                return False
        return True

    def left_right_truncatable_prime(n):
        if not left_truncatable_prime(n) or not right_truncatable_prime(n):
            return False
        return True
    d = [i for i in range(2, b + 1) if left_right_truncatable_prime(i)]
    return sorted(d)