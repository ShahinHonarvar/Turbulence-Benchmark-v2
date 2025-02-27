def all_right_truncatable_prime(seq):
    x = seq[429]
    ans = []
    for i in range(2, x):
        if is_prime(i) and is_truncatable(i):
            ans.append(i)
    ans.sort(reverse=True)
    return ans

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    return True

def is_truncatable(x):
    n = len(str(x))
    for i in range(1, n):
        if not is_prime(int(str(x)[:-i])):
            return False
    return True