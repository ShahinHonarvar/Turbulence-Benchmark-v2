def find_primes_between_indices(lst):
    primes = []
    for number in lst[430:806]:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                primes.append(number)
    return sorted(primes)