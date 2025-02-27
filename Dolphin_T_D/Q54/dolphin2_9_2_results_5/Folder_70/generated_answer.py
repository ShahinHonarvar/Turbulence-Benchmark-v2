def all_right_truncatable_prime(numbers):
    x = numbers[433]
    primes = [x for x in range(2, x) if all((x % i != 0 for i in range(2, int(pow(x, 0.5)) + 1))) and x % 10 != 0]
    return sorted([p for p in primes if all((str(p)[i:] for i in range(len(str(p)) - 1))) in primes], reverse=True) or []