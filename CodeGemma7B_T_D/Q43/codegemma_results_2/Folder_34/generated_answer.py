def find_primes_between_indices(nums):
    primes = []
    for num in nums:
        if num >= 56 and num <= 57:
            if is_prime(num):
                primes.append(num)
    primes.sort(reverse=True)
    return primes

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True