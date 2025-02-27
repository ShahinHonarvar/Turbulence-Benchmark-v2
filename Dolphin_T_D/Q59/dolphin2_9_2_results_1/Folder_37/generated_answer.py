def all_left_truncatable_prime(t):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[35]
    result = []
    for n in range(x, 1, -1):
        if is_prime(n):
            num = n
            while num != 0:
                if not is_prime(num):
                    break
                num //= 10
            else:
                result.append(n)
    return sorted(result, reverse=True)