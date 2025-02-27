def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[0]
    p = []
    for i in range(2, x + 1):
        s = str(i)
        if '0' not in s and (len(s) < 2 or is_prime(int(s[1:-1]))) and (len(s) < 3 or is_prime(int(s[1:] + s[:-1]))):
            p.append(i)
    p.sort()
    return sorted(p, reverse=True)