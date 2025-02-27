def all_left_right_truncatable_prime(x):
    return sorted(all_left_right_truncatable_prime_range(x))

def all_left_right_truncatable_prime_range(x):
    numbers_to_check = range(2, x + 1)
    left_right_truncatable_primes = []

    def is_left_right_truncatable_prime(n):
        stringified_number = str(n).zfill(10).rstrip('0')
        leftmost_digits_to_remove = [stringified_number[0]]
        for i in range(1, 10):
            leftmost_digits_to_remove.append(leftmost_digits_to_remove[-1][:-1])
        for i in range(1, len(leftmost_digits_to_remove)):
            if is_prime(leftmost_digits_to_remove[i - 1]):
                left_right_truncatable_primes.append((leftmost_digits_to_remove[i - 1], n))
        if is_prime(n):
            left_right_truncatable_primes.append((n, n))
    for n in range(2, x + 1):
        is_left_right_truncatable_prime(n)
    return left_right_truncatable_primes