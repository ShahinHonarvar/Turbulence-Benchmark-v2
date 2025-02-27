def find_primes_between_indices(int_list):
    primes = []
    for num in int_list[40:69]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True