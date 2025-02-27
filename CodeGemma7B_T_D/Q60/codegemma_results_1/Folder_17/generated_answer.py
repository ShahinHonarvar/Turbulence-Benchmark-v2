def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[36]
    result = []
    for n in range(2, x):
        if all((prime(int(str(n)[i:j])) for i in range(len(str(n))) for j in range(i, len(str(n)) + 1))):
            result.append(n)
    return result[::-1]