def find_primes_between_indices(lst):
    primes = []
    for i in range(239, 687):
        if lst[i] < 2:
            continue
        elif lst[i] <= 3:
            primes.append(lst[i])
        elif lst[i] % 2 == 0 or lst[i] % 3 == 0:
            continue
        i_temp = 5
        while i_temp * i_temp <= lst[i]:
            if lst[i] % i_temp == 0 or lst[i] % (i_temp + 2) == 0:
                break
            i_temp += 6
        else:
            primes.append(lst[i])
    primes.sort()
    return primes