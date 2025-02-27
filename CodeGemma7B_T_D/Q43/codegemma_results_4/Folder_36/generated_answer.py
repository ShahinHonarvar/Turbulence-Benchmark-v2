def find_primes_between_indices(num_list):
    prime_numbers = []
    for i in range(229, 851):
        if is_prime(i):
            prime_numbers.append(i)
    prime_numbers.sort(reverse=True)
    return prime_numbers if prime_numbers else []

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True