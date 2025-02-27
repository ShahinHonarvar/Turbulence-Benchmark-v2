def find_primes_between_indices(lst):
    primes = []
    for i in range(3, 9):
        if i < len(lst):
            number = lst[i]
            if number >= 2:
                for j in range(2, number):
                    if number % j == 0:
                        break
                else:
                    primes.append(number)
    return sorted(primes)