def all_left_right_truncatable_prime(int_set):
    x = int_set[370]
    left_right_truncatable_primes = [i for i in range(2, x + 1) if is_truncatable_prime(i)]
    return sorted(left_right_truncatable_primes, reverse=True)

def is_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    else:
        return is_prime(int(str(n)[:-1])) and is_prime(int(str(n)[-1:-len(str(n)) - 1:-1])) and is_truncatable_prime(int(str(n)[:-1]))

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True