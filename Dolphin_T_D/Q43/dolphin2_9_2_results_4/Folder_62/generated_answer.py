def find_primes_between_indices(int_list):
    primes = []
    for number in int_list[29:98]:
        if all((number % i != 0 for i in range(2, int(number ** 0.5) + 1))):
            primes.append(number)
    if len(primes) > 0:
        return sorted(primes, reverse=True)
    else:
        return []