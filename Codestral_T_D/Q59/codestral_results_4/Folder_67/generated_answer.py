def all_left_truncatable_prime(numbers):
    x = numbers[71]
    primes = [i for i in range(2, x) if all((int(str(i)[:j]) in [2, 3, 5, 7] for j in range(1, len(str(i)) + 1)))]
    return sorted(primes, reverse=True)