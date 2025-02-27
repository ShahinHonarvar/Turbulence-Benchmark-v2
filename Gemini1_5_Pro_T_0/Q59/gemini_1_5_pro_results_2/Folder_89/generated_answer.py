def all_left_truncatable_prime(numbers):
    x = numbers[97]
    left_truncatable_primes = []
    for num in range(2, x):
        if all((int(str(num)[i:]) in prime_numbers for i in range(len(str(num))))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)