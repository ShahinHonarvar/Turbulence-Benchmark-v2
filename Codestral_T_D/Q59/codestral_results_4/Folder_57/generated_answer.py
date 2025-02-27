def all_left_truncatable_prime(numbers):
    x = numbers[54]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[i:]) > 1 for i in range(len(str(num))))) and all((int(str(num)[i:]) % i != 0 for i in range(1, len(str(num))) for i in range(2, int(str(num)[i:]) // 2 + 1))):
            primes.append(num)
    return sorted(primes, reverse=True)