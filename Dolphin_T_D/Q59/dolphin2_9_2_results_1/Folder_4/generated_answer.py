def all_left_truncatable_prime(t):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[96]
    res = []
    for n in range(x, 1, -1):
        if n < 10 or n == 11 or n == 13 or (n == 17) or (n == 37) or (n == 73) or (n == 97):
            if is_prime(n):
                temp = n
                while temp != 0:
                    if not is_prime(temp):
                        break
                    temp //= 10
                else:
                    res.append(n)
    return res