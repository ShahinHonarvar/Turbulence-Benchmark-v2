def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[74]
    left_right_truncatable_prime = []
    for i in range(2, x + 1):
        s = str(i)
        if '0' in s:
            continue
        while len(s) > 2 and is_prime(int(s)):
            if is_prime(int(s[1:-1])):
                left_right_truncatable_prime.append(int(s))
            s = s[1:-1]
    return sorted(list(set(left_right_truncatable_prime)))