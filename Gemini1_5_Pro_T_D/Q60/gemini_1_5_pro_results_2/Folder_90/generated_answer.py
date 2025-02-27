def all_left_right_truncatable_prime(numbers):
    x = numbers[466]
    primes = []
    for num in range(2, x + 1):
        if all((int(str(num)[i:]) in primes and int(str(num)[:i + 1]) in primes for i in range(len(str(num))))):
            primes.append(num)
    return sorted([prime for prime in primes if '0' not in str(prime)], reverse=True)