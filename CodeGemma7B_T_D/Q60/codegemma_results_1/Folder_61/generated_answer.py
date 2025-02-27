def all_left_right_truncatable_prime(x):
    M = 2
    prime, ans = ([], [])
    while M < x:
        if all_truncatable_prime(M):
            ans.append(M)
        M += 2
    ans.sort(reverse=True)
    return ans

def all_truncatable_prime(M):
    if not is_prime(M):
        return False
    while M >= 10:
        M //= 10
        if not is_prime(M):
            return False
    return True

def is_prime(M):
    if M <= 1:
        return False
    for i in range(4, int(M ** 0.5) + 1, 2):
        if M % i == 0:
            return False
    return True