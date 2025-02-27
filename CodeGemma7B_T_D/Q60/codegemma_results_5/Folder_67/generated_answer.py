def is_prime(n):
    if n % 2 == 0 and n != 2 or (n % 3 == 0 and n != 3) or (n % 5 == 0 and n != 5):
        return False
    if n < 2 or (n % 2 == 0 and n < 9) or (n % 3 == 0 and n < 27) or (n % 5 == 0 and n < 125):
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(x):
    res = []
    for i in range(2, x + 1):
        if is_prime(i) and (not '0' in str(i)):
            if all((is_prime(int(i[:-j])) and is_prime(int(i[j:])) for j in range(1, len(str(i))))):
                res.append(i)
    res.sort(reverse=True)
    return res