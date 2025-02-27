def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    if len(str(n)) <= 1:
        return True
    if str(n)[-1] in ('2', '3', '5', '7'):
        return is_right_truncatable_prime(int(str(n)[:-1]))
    else:
        return False

def all_right_truncatable_prime(numbers):
    x = numbers[77]
    right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes)