def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left_right(n):
    str_n = str(n)
    for i in range(len(str_n)):
        yield int(str_n[i:])

def all_left_right_truncatable_prime(numbers):
    x = numbers[175]
    left_right_truncatable_primes = set()
    for n in range(11, x + 1):
        if is_prime(n) and '0' not in str(n):
            if all((is_prime(i) for i in truncate_left_right(n))):
                left_right_truncatable_primes.add(n)
    return sorted(list(left_right_truncatable_primes))