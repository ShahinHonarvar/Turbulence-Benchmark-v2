def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[760]
    result = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            k = i
            while k > 1:
                if not is_prime(k):
                    break
                k //= 10
            else:
                result.append(i)
    return sorted(result, reverse=True)