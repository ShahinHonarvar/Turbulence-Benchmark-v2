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

def is_truncatable(n):
    d = [int(i) for i in str(n)]
    for i in range(len(d) - 1):
        if d[0] == 0 or d[len(d) - 1] == 0:
            return False
        if not is_prime(int(''.join([str(d[i + j]) for j in range(len(d) - i)]))):
            return False
        if not is_prime(int(''.join([str(d[j]) for j in range(i)]))):
            return False
    return True

def all_left_right_truncatable_prime(n):
    result = []
    for i in range(2, n + 1):
        if is_truncatable(i):
            result.append(i)
    result.sort(reverse=True)
    return result