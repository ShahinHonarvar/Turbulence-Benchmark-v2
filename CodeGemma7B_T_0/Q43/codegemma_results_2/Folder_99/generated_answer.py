def find_primes_between_indices(int_list):
    prime_list = []
    for i in range(187, 272):
        if is_prime(int_list[i]):
            prime_list.append(int_list[i])
    prime_list.sort()
    return prime_list

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True