def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[85]
    result = []
    for i in range(x):
        n = i
        while is_prime(n):
            if is_prime(int(str(n).replace('0', ''))):
                result.append(int(str(n).replace('0', '')))
            if n < 10:
                break
            n = int(str(n)[1:])
    return sorted(list(set(result)))