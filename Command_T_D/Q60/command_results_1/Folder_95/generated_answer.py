def all_left_right_truncatable_prime(n):
    if n[0] > n[1]:
        return []
    x = n[0]

    def is_left_right_truncatable_prime(n):
        if not n % 2 and (not n % 3):
            return False
        if not n % 2:
            return False
        digits = 0
        if n < 10:
            digits = 1
        elif n < 100:
            digits = 2
        elif n < 1000:
            digits = 3
        elif n < 10000:
            digits = 4
        elif n < 100000:
            digits = 5
        elif n < 1000000:
            digits = 6
        elif n < 10000000:
            digits = 7
        elif n < 100000000:
            digits = 8
        elif n < 1000000000:
            digits = 9
        while digits > 1:
            n //= 10
            n //= 10
            if not n % 2 and (not n % 3):
                return False
            if not n % 2:
                return False
            if n < 10:
                digits = 1
            elif n < 100:
                digits = 2
            elif n < 1000:
                digits = 3
            elif n < 10000:
                digits = 4
            elif n < 100000:
                digits = 5
            elif n < 1000000:
                digits = 6
            elif n < 10000000:
                digits = 7
            elif n < 100000000:
                digits = 8
            elif n < 1000000000:
                digits = 9
            if not n % 2 and (not n % 3):
                return False
            if not n % 2:
                return False
            if n < 10:
                digits = 1
            elif n < 100:
                digits = 2
            elif n < 1000:
                digits = 3
            elif n < 10000:
                digits = 4
            elif n < 100000:
                digits = 5
            elif n < 1000000:
                digits = 6
            elif n < 10000000:
                digits = 7
            elif n < 100000000:
                digits = 8
            elif n < 1000000000:
                digits = 9
    left_right_truncatable_primes = []
    for n in range(10, x + 1):
        if is_left_right_truncatable_prime(n):
            left_right_truncatable_primes.append(n)
    return sorted(left_right_truncatable_primes)