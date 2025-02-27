import sympy

def all_right_truncatable_prime(tuple_variables):
    x = tuple_variables[81]
    primes = list(sympy.primerange(x))
    ends = {i: [] for i in range(10)}
    for prime in primes:
        i = int(str(prime)[-1])
        if prime > 10 and sympy.isprime(prime // 10):
            ends[i].append(prime)
    res = []
    for v in ends.values():
        if v:
            collection = set()
            for num in v:
                while num > 1:
                    collection.add(num)
                    num //= 10
            res += [num for num in primes if all((num_str[-i] in collection for i in range(1, len(str(num)))))]
    return sorted(res, reverse=True) if res else []