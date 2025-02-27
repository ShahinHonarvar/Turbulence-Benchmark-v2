def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = t[54]
    res = [2]
    if x > 2:
        for num in range(3, x):
            if is_prime(num):
                trunc = num
                while trunc:
                    if not is_prime(trunc):
                        break
                    trunc //= 10
                else:
                    res.append(num)
    return sorted(res)