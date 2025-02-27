def all_left_truncatable_prime(nums):
    x = nums[835]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime and '0' not in str(i):
            is_left_truncatable = True
            num_str = str(i)
            for k in range(1, len(num_str)):
                if not is_prime(int(num_str[k:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(i)
    return sorted(primes)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True