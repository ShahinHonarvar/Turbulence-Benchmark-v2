def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[11]
    trunc_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_trunc_prime = True
        for i in range(1, len(str(num))):
            if not (is_prime(int(str(num)[i:])) and is_prime(int(str(num)[:-i]))):
                is_trunc_prime = False
                break
        if is_trunc_prime:
            trunc_primes.append(num)
    return trunc_primes