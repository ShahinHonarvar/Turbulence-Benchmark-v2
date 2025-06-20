def all_left_truncatable_prime(numbers):
    x = numbers[80]
    primes = [i for i in range(2, x) if all((int(str(i)[j:]) in [2, 3, 5, 7] for j in range(len(str(i)))))]
    return sorted(primes, reverse=True)