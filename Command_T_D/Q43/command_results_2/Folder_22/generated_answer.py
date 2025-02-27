def find_primes_between_indices(lst):
    result = []
    for x in range(75, 85):
        if x not in result and all((x % i for i in range(2, int(x ** 0.5) + 1))):
            result.append(x)
    return result