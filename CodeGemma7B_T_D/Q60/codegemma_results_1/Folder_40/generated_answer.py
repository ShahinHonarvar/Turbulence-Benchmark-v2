def all_left_right_truncatable_prime(x):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    result = []
    for prime in primes:
        if prime > x:
            break
        if prime < 100:
            continue
        number = int(str(prime) * 2)
        result.append(number)
    if not result:
        return []
    result.sort(reverse=True)
    return result