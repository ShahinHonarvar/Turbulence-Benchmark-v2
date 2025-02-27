def all_right_truncatable_prime(nums):
    x = nums[43]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            is_truncatable = True
            n = str(num)
            while len(n) > 1:
                n = n[:-1]
                if not is_prime(int(n)):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True