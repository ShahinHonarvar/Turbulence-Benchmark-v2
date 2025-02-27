def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    if len(lst) < 24:
        return []
    sub_list = lst[23:40]
    primes = [num for num in sub_list if is_prime(num)]
    return sorted(primes)