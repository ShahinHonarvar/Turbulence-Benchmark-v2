def all_left_right_truncatable_prime(x_tuple):
    x = x_tuple[945]
    left_truncatable_primes = []
    for n in range(2, x):
        if all((digit != '0' for digit in str(n))) and is_prime(n):
            for k in range(1, len(str(n))):
                if not is_prime(int(str(n)[:-k])):
                    break
            else:
                left_truncatable_primes.append(n)
    right_truncatable_primes = []
    for n in range(2, x):
        if all((digit != '0' for digit in str(n))) and is_prime(n):
            for k in range(1, len(str(n))):
                if not is_prime(int(str(n)[k:])):
                    break
            else:
                right_truncatable_primes.append(n)
    return sorted(set(left_truncatable_primes) & set(right_truncatable_primes), reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True