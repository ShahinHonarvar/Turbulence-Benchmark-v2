def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[100]
    left_truncatable_primes = []
    for i in range(10, x):
        str_i = str(i)
        if '0' in str_i:
            continue
        is_left_truncatable_prime = True
        for j in range(len(str_i)):
            if not is_prime(int(str_i[j:])):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime and is_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)