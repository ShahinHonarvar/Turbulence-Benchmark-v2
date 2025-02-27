def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[93]
    left_truncatable_primes = []
    for i in range(10, x):
        str_i = str(i)
        if '0' not in str_i and is_prime(i):
            for j in range(len(str_i)):
                trunc_str = str_i[j:]
                if not is_prime(int(trunc_str)):
                    break
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)