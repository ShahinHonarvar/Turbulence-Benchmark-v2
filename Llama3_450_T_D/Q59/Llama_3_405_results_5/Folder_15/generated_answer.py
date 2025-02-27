def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[6]
    left_truncatable_primes = set()
    for i in range(11, x):
        str_i = str(i)
        if '0' in str_i:
            continue
        is_left_truncatable = True
        for j in range(len(str_i)):
            if not is_prime(int(str_i[j:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.add(i)
    return sorted(list(left_truncatable_primes), reverse=True)