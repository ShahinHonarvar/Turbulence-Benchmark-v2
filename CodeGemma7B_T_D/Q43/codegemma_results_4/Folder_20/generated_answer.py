def find_primes_between_indices(num_list):
    prime_list = []
    for num in num_list[36:41]:
        if is_prime(num):
            prime_list.append(num)
    prime_list = sorted(prime_list, reverse=True)
    return prime_list

def is_prime(num):
    if num <= 1:
        return False
    elif num % 2 == 0:
        return False
    else:
        i = 3
        while i <= int(num ** 0.5) + 1:
            if num % i == 0:
                return False
            i += 2
        return True