def all_left_right_truncatable_prime(numbers):
    x = numbers[35]
    primes = [x for x in range(2, x + 1) if all((x % i != 0 for i in range(2, int(x ** 0.5) + 1)))]
    truncatables = []
    for prime in primes:
        if '0' not in str(prime):
            trunc_left = prime
            while len(str(trunc_left)) > 2:
                trunc_left = int(str(trunc_left)[1:])
                if trunc_left not in primes:
                    break
            trunc_right = prime
            while len(str(trunc_right)) > 2:
                trunc_right = int(str(trunc_right)[:-1])
                if trunc_right not in primes:
                    break
            if len(str(trunc_left)) == 2 and len(str(trunc_right)) == 2:
                truncatables.append(prime)
    return truncatables[::-1] or []