def all_left_right_truncatable_prime(t):
    x = t[945]
    primes = [2]
    result = []
    for num in range(2, x + 1):
        if all((num % p != 0 for p in primes)):
            primes.append(num)
    for prime in primes:
        str_prime = str(prime)
        if '0' in str_prime:
            continue
        while len(str_prime) > 1:
            if int(str_prime[1:-1]) in primes:
                str_prime = str_prime[1:-1]
            else:
                break
        else:
            result.append(prime)
    return sorted(result, reverse=True)