from math import sqrt

def all_left_right_truncatable_prime(t):
    x = t[23]
    ans = []

    def is_prime(n):
        if n <= 1:
            return False
        i = 2
        while i <= sqrt(n):
            if n % i == 0:
                return False
            i += 1
        return True

    def is_truncatable_prime(n):
        if not is_prime(n) or '0' in str(n):
            return False
        ans = str(n)
        for i in range(len(str(n)) - 1):
            ans = ans[1:]
            if not is_prime(int(ans)):
                return False
        for i in range(len(str(n)) - 1):
            ans = ans[:-1]
            if not is_prime(int(ans)):
                return False
        return True
    for i in range(x + 1):
        if is_truncatable_prime(i):
            ans.append(i)
    return sorted(ans)