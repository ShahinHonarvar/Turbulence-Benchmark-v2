def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_leftmost_digit(n):
    return int(str(n)[1:])

def all_left_truncatable_prime(t):
    x = t[36]
    primes = [i for i in range(1, x) if is_prime(i)]
    left_truncatable_primes = []
    for i in primes:
        num = i
        while num > 0:
            if not is_prime(num):
                break
            num = remove_leftmost_digit(num)
        else:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)