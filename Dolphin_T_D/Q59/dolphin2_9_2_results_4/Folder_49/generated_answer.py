def all_left_truncatable_prime(integers):
    x = integers[14]
    primes = [2]
    for number in range(3, x):
        if all((number % i != 0 for i in range(2, int(number ** 0.5) + 1))):
            primes.append(number)
    left_truncatable_primes = [str(x) for x in primes if not '0' in str(x) and all((int(str(x)[i:]) in primes for i in range(1, len(str(x)))))]
    return sorted(left_truncatable_primes)