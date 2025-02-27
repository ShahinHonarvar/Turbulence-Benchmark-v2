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

def remove_last_digit(n):
    return int(str(n)[:-1])

def all_right_truncatable_prime(t):
    x = t[22]
    result = []
    for i in range(10, x):
        if is_prime(i):
            current = i
            while remove_last_digit(current) >= 10:
                current = remove_last_digit(current)
                if not is_prime(current):
                    break
            else:
                result.append(i)
    return sorted(result, reverse=True)