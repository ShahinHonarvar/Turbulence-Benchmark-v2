def all_left_truncatable_prime(numbers):
    x = numbers[70]
    left_truncatable_primes = []
    for num in range(2, x):
        if all((int(str(num)[:i]) in [2, 3, 5, 7] for i in range(1, len(str(num))))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)