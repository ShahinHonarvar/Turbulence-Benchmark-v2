def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    prime_numbers = []
    for num in lst[20:26]:
        if is_prime(num):
            prime_numbers.append(num)
    prime_numbers.sort(reverse=True)
    return prime_numbers