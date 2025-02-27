def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[46]
    left_truncatable_primes = set()
    for i in range(11, x):
        str_i = str(i)
        if '0' in str_i:
            continue
        if not is_prime(i):
            continue
        for j in range(1, len(str_i)):
            if not is_prime(int(str_i[j:])):
                break
        else:
            left_truncatable_primes.add(i)
    return sorted(list(left_truncatable_primes), reverse=True)