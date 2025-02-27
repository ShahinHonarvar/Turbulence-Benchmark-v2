def all_left_truncatable_prime(tp):
    x = tp[87]
    primes = [i for i in range(2, x) if all((str(i)[1:] != '0' and int(str(i)[:-j]) in primes for j in range(1, len(str(i)))))]
    return sorted(primes)