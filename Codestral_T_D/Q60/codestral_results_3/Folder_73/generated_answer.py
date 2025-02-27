def all_left_right_truncatable_prime(t):
    x = t[97]
    primes = []
    for possiblePrime in range(2, x + 1):
        if all((possiblePrime % i != 0 for i in range(2, int(possiblePrime ** 0.5) + 1))) and '0' not in str(possiblePrime):
            prime_str = str(possiblePrime)
            while len(prime_str) > 1:
                prime_str = prime_str[1:]
                if int(prime_str) not in primes:
                    break
                prime_str = prime_str[:-1]
                if int(prime_str) not in primes:
                    break
            else:
                primes.append(possiblePrime)
    return sorted(primes)