def all_right_truncatable_prime(nums):
    x = nums[10]
    primes = []
    for i in range(2, x):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            truncatable = True
            num_str = str(i)
            while len(num_str) > 0:
                if not is_prime(int(num_str)):
                    truncatable = False
                    break
                num_str = num_str[:-1]
            if truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True