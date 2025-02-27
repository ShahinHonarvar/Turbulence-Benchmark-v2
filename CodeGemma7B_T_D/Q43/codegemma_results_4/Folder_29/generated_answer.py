def find_primes_between_indices(num_list):
    prime_nums = sorted([num for num in num_list[24:33] if is_prime(num)], reverse=True)
    return prime_nums if prime_nums else []

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True