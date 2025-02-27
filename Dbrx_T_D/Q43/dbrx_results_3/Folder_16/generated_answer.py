def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(input_list):
    prime_list = sorted(set((i for i in input_list[424:553] if is_prime(i))), reverse=True)
    return prime_list