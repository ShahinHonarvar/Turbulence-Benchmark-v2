def all_left_truncatable_prime(numbers):
    x = numbers[74]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[i:]) in primes for i in range(len(str(num))))):
            primes.append(num)
    return sorted(primes)