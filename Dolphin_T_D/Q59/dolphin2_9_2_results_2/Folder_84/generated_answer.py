def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[630]
    result = []
    for i in range(10 ** (x.bit_length() - 1), x):
        if all((is_prime(int(str(i)[j:])) for j in range(len(str(i))))):
            result.append(i)
    return sorted(result, reverse=True)