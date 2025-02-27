def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
    x = t[18]
    result = [n for n in range(x) if is_prime(n) and (not '0' in str(n)) and all((is_prime(int(str(n)[i:])) for i in range(1, len(str(n)))))]
    return sorted(result, reverse=True)