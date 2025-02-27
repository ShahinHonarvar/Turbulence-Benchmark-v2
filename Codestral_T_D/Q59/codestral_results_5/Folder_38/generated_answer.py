def all_left_truncatable_prime(numbers):
    x = numbers[28]
    primes = []
    for num in range(2, x):
        if '0' not in str(num) and all((int(str(num)[i:]) > 1 for i in range(1, len(str(num))))):
            primes.append(num)
    return sorted(primes)