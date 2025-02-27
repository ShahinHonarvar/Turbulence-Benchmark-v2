def find_primes_between_indices(nums):
    primes = []
    for num in nums[61:81]:
        if is_prime(num):
            primes.append(num)
    primes.sort(reverse=True)
    return primes

def is_prime(num):
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num ** 0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True