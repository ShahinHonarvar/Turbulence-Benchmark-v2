def all_left_truncatable_prime(numbers):
    x = numbers[64]
    primes = [i for i in range(x) if all((int(str(i)[j:]) in [2, 3, 5, 7] + [i for i in range(11, int(str(i)[j:]), 2) if all((i % j != 0 for j in range(3, int(i ** 0.5) + 1, 2)))] for j in range(len(str(i)))))]
    return sorted(primes, reverse=True)