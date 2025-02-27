def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[20]
    left_truncatable_primes = []
    for possiblePrime in range(10, x):
        if '0' in str(possiblePrime):
            continue
        str_num = str(possiblePrime)
        is_left_truncatable_prime = True
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime and is_prime(possiblePrime):
            left_truncatable_primes.append(possiblePrime)
    return sorted(left_truncatable_primes, reverse=True)