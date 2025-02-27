def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def remove_rightmost_digit(n):
    return int(str(n)[:-1])

def all_right_truncatable_prime(t):
    x = t[39]
    rtp = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j > 0:
                if not is_prime(j):
                    break
                j = remove_rightmost_digit(j)
            if j == 0:
                rtp.append(i)
    return sorted(rtp)