def all_left_truncatable_prime(t):
    x = t[70]
    primes = [2]
    for num in range(3, x, 2):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    left_truncatable_primes = []
    for prime in primes:
        num_str = str(prime)
        if '0' not in num_str:
            truncated_nums = [int(num_str[i:]) for i in range(len(num_str))]
            if all((num in primes for num in truncated_nums)):
                left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)