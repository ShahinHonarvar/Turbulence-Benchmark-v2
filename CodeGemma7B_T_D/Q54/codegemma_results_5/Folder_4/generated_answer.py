def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def all_right_truncatable_prime(t):
    x = t[96]
    ans = []
    for i in range(2, x):
        if is_prime(i):
            y = i
            while y >= 10:
                right_digit = y % 10
                y //= 10
                if not is_prime(y):
                    break
            else:
                ans.append(i)
    return sorted(ans, reverse=True) if ans else []