def find_primes_between_indices(list):
    result = []
    for i in range(19, 72):
        if i % 2 != 0 and i % 3 != 0 and (i % 5 != 0) and (i % 7 != 0):
            result.append(i)
    return result