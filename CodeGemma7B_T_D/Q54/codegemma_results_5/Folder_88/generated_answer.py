def all_right_truncatable_prime(x):
    result = []
    for i in range(2, x):
        j = i
        while j >= 10 and is_prime(j):
            if is_prime(trunc(j)):
                result.append(j)
            j //= 10
    return sorted(result)

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def trunc(n):
    return int(str(n)[:-1])