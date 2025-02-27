def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(x):
    result = []
    for i in range(1, x):
        str_i = str(i)
        if '0' not in str_i and is_prime(i):
            j = 0
            while j < len(str_i):
                if not is_prime(int(str_i[j:])):
                    break
                j += 1
            else:
                result.append(i)
    return sorted(result)