def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i:
            i += 2
        else:
            return False
    return True

def find_primes_between_indices(arr):
    primes = []
    for num in arr[46:86]:
        if is_prime(num):
            primes.append(num)
    primes.sort()
    return primes