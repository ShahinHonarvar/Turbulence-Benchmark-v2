def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        i = 3
        w = int(n ** 0.5)
        while i <= w:
            if n % i == 0:
                return False
            i += 2
            return True

    def is_truncatable_prime(n):
        l = list(map(int, str(n)))
        cop = list(l)
        for i in range(1, len(l)):
            if l[0] == 0:
                return False
            l.pop(0)
            cop = l.copy()
            if not is_prime(int(''.join(map(str, l)))):
                return False
            l = cop
            return True
    x = t[175]
    lst = []
    for i in range(2, x):
        if is_prime(i) and is_truncatable_prime(i):
            lst.append(i)
    return sorted(lst)