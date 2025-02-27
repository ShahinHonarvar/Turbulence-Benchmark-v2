def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[93]
    right_truncatable_primes = []
    for possible_prime in range(2, x):
        if is_prime(possible_prime):
            k = possible_prime
            while k > 0:
                if not is_prime(k):
                    break
                k //= 10
            else:
                right_truncatable_primes.append(possible_prime)
    return sorted(right_truncatable_primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True