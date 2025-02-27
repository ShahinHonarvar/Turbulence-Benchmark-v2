def all_right_truncatable_prime(nums):
    x = nums[22]
    primes = []
    for i in range(2, x):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            right_truncatable = True
            num = str(i)
            while len(num) > 1:
                num = num[:-1]
                if not is_prime(int(num)):
                    right_truncatable = False
                    break
            if right_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True