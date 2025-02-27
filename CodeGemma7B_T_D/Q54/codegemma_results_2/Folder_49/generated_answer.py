def all_right_truncatable_prime(args):
    x = args[14]
    ans = []
    for i in range(2, x):
        if is_prime(i):
            for j in range(i % 10, i + 1, +1):
                if is_prime(j):
                    ans.append(j)
    return sorted(ans)

def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return False
    candidate = 3
    while candidate ** 2 <= x:
        if x % candidate == 0:
            return False
        candidate += 2
    return True