def find_primes_between_indices(int_list):
    prime_list = []
    for x in range(31, 68):
        if is_prime(x):
            prime_list.append(x)
    return prime_list

def is_prime(num):
    if num <= 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True