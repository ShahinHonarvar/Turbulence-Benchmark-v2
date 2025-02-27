def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[97]
    prime_numbers = [n for n in range(2, x + 1) if all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))]
    left_right_truncatable = []
    for p in prime_numbers:
        if '0' not in str(p) and len(str(p)) > 1 and all((str(p)[i:j] in prime_numbers for i in range(len(str(p))) for j in range(i + 2, len(str(p)) + 1))):
            left_right_truncatable.append(p)
    return left_right_truncatable