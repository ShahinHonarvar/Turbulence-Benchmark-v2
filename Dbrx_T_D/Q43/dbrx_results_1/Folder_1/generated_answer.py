def find_primes_between_indices(lst):
    primes = []
    for i in range(len(lst)):
        if lst[i] > 1:
            is_prime = True
            for j in range(2, int(lst[i] ** 0.5) + 1):
                if lst[i] % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(lst[i])
    if len(primes) >= 3:
        return sorted(primes[87:90])
    else:
        return []