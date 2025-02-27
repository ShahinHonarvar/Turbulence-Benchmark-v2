def all_left_right_truncatable_prime(tu):
    sep = int(tu[70])
    ans = []

    def isprime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def lefttrunc(n):
        n = str(n)
        if n[0] == '0':
            return False
        for i in range(len(n)):
            if not isprime(int(n[i:len(n)])):
                return False
        return True

    def righttrunc(n):
        n = str(n)
        if n[-1] == '0':
            return False
        for i in range(len(n)):
            if not isprime(int(n[0:len(n) - i])):
                return False
        return True
    for i in range(sep, 1, -1):
        if lefttrunc(i) and righttrunc(i):
            ans.append(i)
    return sorted(ans, reverse=True)