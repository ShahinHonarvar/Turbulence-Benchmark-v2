def find_primes_between_indices(lst):
    primes = []
    for i in range(21, 98):
        number = lst[i]
        if number > 1:
            for j in range(2, number):
                if number % j == 0:
                    break
            else:
                primes.append(number)
    return sorted(primes)