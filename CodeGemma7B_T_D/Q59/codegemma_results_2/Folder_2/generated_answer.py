def all_left_truncatable_prime(x):
    x = set(x)
    x = {i for i in x if '0' not in str(i)}
    result = []
    for i in x:
        if is_prime(i):
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[j:])):
                    break
            else:
                result.append(i)
    return sorted(result)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True