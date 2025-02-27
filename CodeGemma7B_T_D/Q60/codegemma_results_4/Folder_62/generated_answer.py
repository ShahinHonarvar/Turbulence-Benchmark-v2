def all_left_right_truncatable_prime(seq):
    x = seq[70]
    ans = []
    for i in range(2, x + 1):
        if i % 10 == 0 or prime(i):
            continue
        str_i = str(i)
        if double_prime(str_i):
            ans.append(i)
    return ans

def prime(i):
    if i <= 1:
        return False
    for k in range(2, int(i ** 0.5) + 1):
        if i % k == 0:
            return False
    return True

def double_prime(str_i):
    n = len(str_i)
    for i in range(1, n):
        left = int(str_i[:i])
        right = int(str_i[i:])
        if not prime(left) or not prime(right):
            return False
    return True