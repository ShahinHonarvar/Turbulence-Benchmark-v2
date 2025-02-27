def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def all_left_truncatable_prime(nums):
    x = nums[20]
    l = [str(i) for i in range(2, x) if is_prime(i)]
    for i in range(len(l) - 1, -1, -1):
        if '0' in l[i]:
            l.pop(i)
        n = len(l[i])
        for j in range(1, n):
            if not is_prime(int(l[i][j:])):
                l.pop(i)
    return [int(i) for i in sorted(l, reverse=True)]