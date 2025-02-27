def all_right_truncatable_prime(t):
    x = t[67]

    def is_prime(n):
        if n > 3 and n % 2 == 0:
            return n == 2
        divisor = 3
        while divisor * divisor <= n and n % divisor != 0:
            divisor += 2
        return divisor * divisor > n
    result = []
    for n in range(2, x):
        if is_prime(n):
            if len(str(n)) > 1:
                n1 = int(str(n)[1:])
                if is_prime(n1):
                    n2 = int(str(n1)[1:])
                    if is_prime(n2):
                        n3 = int(str(n2)[1:])
                        if is_prime(n3):
                            n4 = int(str(n3)[1:])
                            if is_prime(n4):
                                result.append(n)
    result.sort(reverse=True)
    return result