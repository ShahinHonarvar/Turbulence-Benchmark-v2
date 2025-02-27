def all_left_truncatable_prime(numbers):
    x = numbers[23]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[i:]) in [i for i in range(2, int(max(str(num)[i:]) ** 0.5) + 1) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))] for i in range(len(str(num))))):
            primes.append(num)
    return primes