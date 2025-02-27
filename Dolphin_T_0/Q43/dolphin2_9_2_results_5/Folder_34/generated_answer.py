def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    prime_numbers = [num for num in lst[56:58] if is_prime(num)]
    prime_numbers.sort(reverse=True)
    return prime_numbers