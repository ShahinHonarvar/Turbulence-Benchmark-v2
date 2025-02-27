def all_left_truncatable_prime(numbers):
    x = numbers[30]
    primes = [i for i in range(2, x) if all((int(str(i)[j:]) in set(range(2, x)) for j in range(len(str(i)))))]
    return sorted(primes, reverse=True)