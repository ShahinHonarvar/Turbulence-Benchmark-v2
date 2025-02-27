def all_right_truncatable_prime(nums):
    x = nums[97]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            is_truncatable = True
            num_str = str(i)
            while len(num_str) > 1:
                num_str = num_str[:-1]
                if not is_prime(int(num_str)):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    return sorted(primes)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True