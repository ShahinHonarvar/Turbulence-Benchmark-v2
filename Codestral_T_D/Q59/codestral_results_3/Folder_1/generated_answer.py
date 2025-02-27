def all_left_truncatable_prime(numbers):
    x = numbers[20]
    primes = [2]
    for i in range(3, x, 2):
        if all((i % j != 0 for j in range(3, int(i ** 0.5) + 1, 2))):
            primes.append(i)
    left_truncatable_primes = []
    for prime in primes:
        num = str(prime)
        if '0' in num:
            continue
        truncated_nums = [int(num[i:]) for i in range(len(num))]
        if all((num in primes for num in truncated_nums)):
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)