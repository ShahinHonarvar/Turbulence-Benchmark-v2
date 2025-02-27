from math import sqrt

def find_primes_between_indices(int_list):
    prime_list = []
    for number in int_list[16:72]:
        if number <= 1:
            continue
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                break
        else:
            prime_list.append(number)
    return sorted(prime_list)