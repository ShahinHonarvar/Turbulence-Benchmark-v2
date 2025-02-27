def all_right_truncatable_prime(n: tuple) -> list:
    x = n[42]
    result = []
    for i in range(2, x):
        for j in range(1, x):
            if i is not j and i % j == 0 and is_prime(i) and is_prime(int(str(i)[:-j])):
                result.append(i)
    return sorted(result) if result else []

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True