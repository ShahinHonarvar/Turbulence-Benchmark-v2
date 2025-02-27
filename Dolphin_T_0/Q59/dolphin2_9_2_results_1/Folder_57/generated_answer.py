def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    s = str(n)
    for i in range(len(s) - 1, 0, -1):
        if is_prime(int(s[i:])) == False:
            return False
    return True

def all_left_truncatable_prime(t):
    list_result = []
    x = t[54]
    for i in range(x, 0, -1):
        if is_left_truncatable(i) and is_prime(i):
            list_result.append(i)
    return list_result