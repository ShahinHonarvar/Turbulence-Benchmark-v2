def all_left_truncatable_prime(numbers):
    x = numbers[100]
    primes = [2]
    for num in range(3, x, 2):
        if all((int(str(num)[i:]) in primes for i in range(1, len(str(num))))):
            primes.append(num)
    return sorted(primes, reverse=True)