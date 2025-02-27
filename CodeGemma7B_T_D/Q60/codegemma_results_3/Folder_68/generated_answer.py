def all_left_right_truncatable_prime(n):

    def isprime(x):
        if x == 2 or x == 3:
            return True
        elif x <= 1 or x % 2 == 0 or x % 3 == 0:
            return False
        i = 5
        while i * i <= x:
            if x % i == 0 or x % (i + 2) == 0:
                return False
            i += 6
        return True

    def lefttrunc(x):
        while x >= 10:
            x //= 10
        return x

    def righttrunc(x):
        while x % 10 == 0:
            x //= 10
        return x
    s = [str(x) for x in range(2, n + 1) if '0' not in str(x) and isprime(x)]
    a = []
    for x in s:
        flag = True
        for i in range(1, len(x) - 1):
            if not (isprime(int(x[i:len(x)])) and isprime(lefttrunc(int(x[i:len(x)])))):
                flag = False
                break
        if flag:
            a.append(int(x))
    a.sort(reverse=True)
    return a