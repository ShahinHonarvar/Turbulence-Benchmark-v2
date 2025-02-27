def find_primes_between_indices(arr):
    result = [x for x in arr[31:68] if is_prime(x)]
    result.sort(reverse=True)
    return result

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True