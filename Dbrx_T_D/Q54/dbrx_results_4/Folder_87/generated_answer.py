def all_right_truncatable_prime(t):
    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101}
    x = 103
    result = []
    for p in primes:
        if p >= x:
            break
        for i in range(1, len(str(p)) + 1):
            if int(str(p)[:-i]) not in primes:
                break
            if i == len(str(p)):
                result.append(p)
    return sorted(result, reverse=True)