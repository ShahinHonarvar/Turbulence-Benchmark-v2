def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def truncate_right(n):
    while n > 9:
        n /= 10
    return int(n)

def all_right_truncatable_prime(t):
    x = sorted(t, key=lambda x: x[97])[97]
    result = []
    for i in range(2, x):
        j = i
        while j > 0:
            if not is_prime(j):
                break
            j = truncate_right(j)
        else:
            result.append(i)
    return sorted(result, reverse=True)