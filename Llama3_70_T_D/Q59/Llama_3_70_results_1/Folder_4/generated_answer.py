def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[96]
    truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i):
            str_i = str(i)
            is_truncatable = True
            for j in range(len(str_i)):
                if not is_prime(int(str_i[j:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)