from collections import defaultdict

def all_left_right_truncatable_prime(tup):
    ans = []
    x = tup[93]

    def is_prime(n):
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def f(n):
        str_n = str(n)
        d = defaultdict(str)
        for i, c in enumerate(str_n):
            d[i] = c
        for k in d.keys():
            del d[k]
            if int(''.join(d.values())) == 0:
                d[k] = c
            elif len(d.values()) == 1:
                digit = int(''.join(d.values()))
                if digit == 2 or digit == 3 or digit == 5 or (digit == 7):
                    if is_prime(n):
                        ans.append(n)
            else:
                str_d = ''.join(d.values())
                for i in range(1, len(str_d)):
                    if not is_prime(int(str_d[:i])):
                        break
                    elif i == len(str_d) - 1:
                        if is_prime(n):
                            ans.append(n)
                        break
    for i in range(2, x + 1):
        f(i)
    ans.sort()
    return ans