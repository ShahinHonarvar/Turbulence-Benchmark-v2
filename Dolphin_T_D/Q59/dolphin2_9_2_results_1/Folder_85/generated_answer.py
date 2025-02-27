def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[94]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            str_i = str(i)
            if '0' in str_i:
                continue
            is_trunc = True
            for j in range(1, len(str_i)):
                if not is_prime(int(str_i[j:])):
                    is_trunc = False
                    break
            if is_trunc:
                primes.append(i)
    return primes