def all_left_truncatable_prime(numbers):
    x = numbers[29]
    primes = [2]
    ltp_primes = []
    for num in range(3, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    for prime in primes:
        str_prime = str(prime)
        if '0' not in str_prime:
            truncated_primes = [int(str_prime[i:]) for i in range(len(str_prime))]
            if all((p in primes for p in truncated_primes)):
                ltp_primes.append(prime)
    return sorted(ltp_primes)