def all_left_truncatable_prime(nums):
    x = nums[784]
    primes = []
    for i in range(2, x):
        s = str(i)
        is_prime = True
        for j in range(1, len(s)):
            if not is_prime_number(int(s[j:])):
                is_prime = False
                break
        if is_prime and is_prime_number(i):
            primes.append(i)
    return sorted(primes)

def is_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True