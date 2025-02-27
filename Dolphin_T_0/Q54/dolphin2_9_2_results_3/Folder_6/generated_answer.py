def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[74]
    result = []
    for i in range(1, x):
        if is_prime(i):
            temp = i
            while temp > 1:
                temp //= 10
                if not is_prime(temp):
                    break
                if temp == 1:
                    result.append(i)
    return sorted(result)