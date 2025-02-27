from math import sqrt

def find_primes_between_indices(arr):
    prime_list = []
    begin, end = (89, 93)
    for i in range(begin, end + 1):
        is_prime = True
        if arr[i] <= 1:
            is_prime = False
        for j in range(2, int(sqrt(arr[i])) + 1):
            if arr[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(arr[i])
    prime_list.sort(reverse=True)
    if not prime_list:
        return []
    return prime_list