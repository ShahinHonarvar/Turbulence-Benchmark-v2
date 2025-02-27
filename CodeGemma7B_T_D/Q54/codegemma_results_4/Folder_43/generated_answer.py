def all_right_truncatable_prime(tup):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    result = []
    x = tup[89]
    for prime in primes:
        if prime >= x:
            break
        for i in range(1, 8):
            num = prime
            for j in range(i):
                num //= 10
            if num not in primes:
                break
        else:
            result.append(prime)
    return sorted(result, reverse=True)