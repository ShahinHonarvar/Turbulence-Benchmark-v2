def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(x):
    result = []
    for num in range(1, x):
        num_str = str(num)
        if num_str[0] == '0':
            continue
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])):
                break
        else:
            result.append(num)
    return sorted(result)