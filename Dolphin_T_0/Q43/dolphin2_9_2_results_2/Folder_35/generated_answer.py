def find_primes_between_indices(input_list):
    primes = []
    for number in input_list:
        if 112 <= input_list.index(number) <= 361:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                primes.append(number)
    primes.sort(reverse=True)
    return primes if primes else []