def find_primes_between_indices(lst):
    primes = []
    for i, num in enumerate(lst[87:90]):
        if num > 1 and all((num % j != 0 for j in range(2, num))):
            primes.append(num)
    return sorted(primes)