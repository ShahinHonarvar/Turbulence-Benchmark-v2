def find_primes_between_indices(list):
    list = list[59:97]
    list = sorted(list, reverse=True)
    if len(list) == 0:
        return []