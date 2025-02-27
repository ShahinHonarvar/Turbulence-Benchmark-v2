def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[767]
    left_truncatable_primes = []
    for i in range(10, x):
        if '0' in str(i):
            continue
        str_i = str(i)
        truncatable = True
        for j in range(len(str_i)):
            if not is_prime(int(str_i[j:])):
                truncatable = False
                break
        if truncatable and is_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)