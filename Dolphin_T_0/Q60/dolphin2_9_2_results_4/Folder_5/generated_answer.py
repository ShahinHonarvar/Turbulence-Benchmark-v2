def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(y):
    P = []
    left = 2
    while left <= y[0]:
        if is_prime(left) and left < 10 and (left not in P):
            P.append(left)
        elif is_prime(left) and left >= 10:
            s = str(left)
            if set(s) == set(str(10 * int(s[1:-1]))):
                P.append(left)
        left += 1
    return P