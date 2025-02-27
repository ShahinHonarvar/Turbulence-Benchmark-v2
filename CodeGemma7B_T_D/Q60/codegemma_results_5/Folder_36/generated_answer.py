import math

def all_left_right_truncatable_prime(x):
    t = tuple(range(10 ** (len(str(x)) - 1), x + 1))
    ans = []
    for n in t:
        if len(str(n)) < 3 and int(str(n)) in [2, 3, 5, 7]:
            ans.append(n)
            continue
        if '0' in str(n) or int(str(n)[-1]) in [2, 4, 5, 6, 8] or int(str(n)[-2:]) not in [3, 7]:
            continue
        l, r = (int(str(n)[:-1]), int(str(n)[-2:]))

        def is_prime(n):
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
            return True
        if is_prime(n) and is_prime(l) and is_prime(r):
            if l == 2 and r == 3:
                continue
            ans.append(n)
    return ans