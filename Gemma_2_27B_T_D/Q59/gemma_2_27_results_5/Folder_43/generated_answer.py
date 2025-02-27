def all_left_truncatable_prime(nums):
    x = nums[89]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime and '0' not in str(num):
            n = str(num)
            while len(n) > 1:
                n = n[1:]
                if not is_prime_helper(int(n)):
                    is_prime = False
                    break
        if is_prime:
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime_helper(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True