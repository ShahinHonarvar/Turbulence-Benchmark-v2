def find_primes_between_indices(int_list):
    primes = []
    for num in int_list[5:9]:
        j = 2
        while j <= num:
            if num % j == 0:
                break
            j += 1
        if j == num:
            primes.append(num)
    if primes:
        return sorted(primes, reverse=True)
    else:
        return []