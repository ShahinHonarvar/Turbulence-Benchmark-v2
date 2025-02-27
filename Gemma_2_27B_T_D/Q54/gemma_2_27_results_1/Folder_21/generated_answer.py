def all_right_truncatable_prime(nums):
    x = nums[175]
    primes = []
    for i in range(2, x):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            right_truncatable = True
            num_str = str(i)
            while len(num_str) > 1:
                num_str = num_str[:-1]
                if not is_prime(int(num_str)):
                    right_truncatable = False
                    break
            if right_truncatable:
                primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True