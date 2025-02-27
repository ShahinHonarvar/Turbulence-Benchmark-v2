from math import sqrt

def find_primes_between_indices(num_list):
    prime_nums = []
    for i in range(17, 80):
        is_prime = True
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(i)
    prime_nums.sort(reverse=True)
    return prime_nums