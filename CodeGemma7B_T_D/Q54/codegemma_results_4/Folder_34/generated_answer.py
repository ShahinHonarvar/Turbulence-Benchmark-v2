def all_right_truncatable_prime(n):
    result = []
    for i in range(n):
        for j in range(i):
            if prime(i) and prime(int(str(i)[:-1])):
                result.append(i)
    return sorted(list(set(result))[::-1])

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True