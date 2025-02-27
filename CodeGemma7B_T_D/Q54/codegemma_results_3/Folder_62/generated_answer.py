import math

def is_prime(n):
    if n % 2 == 0:
        return False
    elif n == 2:
        return True
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_right_truncatable_primes(x):
    result = []
    for i in range(2, x):
        if is_prime(i):
            str_i = str(i)
            for j in range(1, len(str_i)):
                if not is_prime(int(str_i[:-j])):
                    break
            else:
                result.append(i)
    return sorted(result)

def all_right_truncatable_prime(x):
    return (get_right_truncatable_primes(x)[0], get_right_truncatable_primes(x)[-1])