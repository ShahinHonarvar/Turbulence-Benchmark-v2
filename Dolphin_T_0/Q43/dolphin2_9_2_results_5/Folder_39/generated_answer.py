def find_primes_between_indices(in_list):
    primes = []
    for number in in_list[69:81]:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                primes.append(number)
    return primes