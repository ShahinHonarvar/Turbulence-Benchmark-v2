def all_left_truncatable_prime(tup):
    x = tup[42]
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, i)))]
    result = []
    for i in primes:
        str_i = str(i)
        if '0' not in str_i:
            left_truncatable = True
            for j in range(1, len(str_i)):
                if int(str_i[:j]) not in primes:
                    left_truncatable = False
                    break
            if left_truncatable:
                result.append(i)
    return sorted(result)