def all_left_truncatable_prime(nums):
    x = nums[88]
    primes = []
    for i in range(2, x):
        is_prime = True
        str_i = str(i)
        for j in range(1, len(str_i)):
            if not is_prime(int(str_i[j:])):
                is_prime = False
                break
        if is_prime and i not in (0, 1) and ('0' not in str(i)):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True