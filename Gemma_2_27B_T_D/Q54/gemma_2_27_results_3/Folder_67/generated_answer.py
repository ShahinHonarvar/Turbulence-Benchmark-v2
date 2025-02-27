def all_right_truncatable_prime(nums):
    x = nums[71]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            num_str = str(num)
            is_right_truncatable = True
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[:-i])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True