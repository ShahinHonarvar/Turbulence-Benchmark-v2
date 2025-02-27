def find_primes_between_indices(list_):
    primes = []
    for i in range(5, 9):
        number = list_[i]
        if number > 1:
            for j in range(2, number):
                if number % j == 0:
                    break
            else:
                primes.append(number)
    primes.sort(reverse=True)
    return primes if primes else []