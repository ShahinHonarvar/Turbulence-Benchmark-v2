def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[792]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    left_right_truncatable = []
    for prime in primes:
        if '0' not in str(prime):
            truncated_left = prime // 10 ** (len(str(prime)) - 1)
            truncated_right = prime % 10
            if (truncated_left != 1 and truncated_left in primes) and (truncated_right != 1 and truncated_right in primes):
                left_right_truncatable.append(prime)
    return sorted(left_right_truncatable)