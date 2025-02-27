def all_right_truncatable_prime(t):
    x = t[79]

    def prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0 or n <= 1:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_right_truncatable(n):
        if prime(n):
            for i in range(1, len(str(n))):
                if prime(int(str(n)[:-i])):
                    continue
                else:
                    return False
            return True
        return False
    list = []
    for i in range(2, x):
        if is_right_truncatable(i) == True:
            list.append(i)
    return sorted(list, reverse=True)