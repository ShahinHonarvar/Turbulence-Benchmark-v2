def all_left_truncatable_prime(t):
    x = t[100]
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for prime in primes:
        str_prime = str(prime)
        is_prime = True
        for i in range(1, len(str_prime)):
            if int(str_prime[:i]) not in primes:
                is_prime = False
                break
        if is_prime:
            result.append(prime)
    result.sort(reverse=True)
    return result