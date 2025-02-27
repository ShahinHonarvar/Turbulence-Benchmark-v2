def is_prime(n):
    if n > 1:
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    return False

def all_left_truncatable_prime(t):
    x = t[87]
    ret = []
    for i in range(2, x):
        if is_prime(i):
            temp = i
            while temp:
                if temp != i:
                    if not is_prime(temp):
                        break
                temp //= 10
                if temp == 0:
                    ret.append(i)
    return sorted(ret)