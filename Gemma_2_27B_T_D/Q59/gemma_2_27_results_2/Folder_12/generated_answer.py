def all_left_truncatable_prime(nums):
    x = nums[70]
    primes = []
    for num in range(2, x):
        is_prime = True
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not is_prime_number(int(str_num[i:])):
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True