def all_left_truncatable_prime(numbers):
    x = numbers[55]
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    lt_primes = [p for p in primes if '0' not in str(p) and all((int(str(p)[i:]) in primes for i in range(1, len(str(p)))))]
    return sorted(lt_primes, reverse=True)