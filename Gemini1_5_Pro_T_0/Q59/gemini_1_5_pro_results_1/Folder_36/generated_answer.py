def all_left_truncatable_prime(numbers):
    x = numbers[992]
    left_truncatable_primes = []
    for num in range(2, x):
        if all((int(str(num)[i:]) in [2, 3, 5, 7] or (int(str(num)[i:]) > 7 and all((int(str(num)[i:]) % j for j in range(3, int(int(str(num)[i:]) ** 0.5) + 1, 2)))) for i in range(len(str(num))))):
            left_truncatable_primes.append(num)
    return left_truncatable_primes