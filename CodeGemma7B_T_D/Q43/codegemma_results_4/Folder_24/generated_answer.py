def find_primes_between_indices(lst):
    primes = []
    x = 38
    y = 55
    for i in range(x, y + 1):
        if lst[i] == 2 or lst[i] == 3 or lst[i] == 5 or (lst[i] == 7):
            primes.append(lst[i])
        elif lst[i] % 2 != 0 and lst[i] % 3 != 0 and (lst[i] % 5 != 0) and (lst[i] % 7 != 0):
            primes.append(lst[i])
    primes.sort(reverse=True)
    return primes