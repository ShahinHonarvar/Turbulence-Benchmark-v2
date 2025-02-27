def all_left_truncatable_prime(nums):
    x = nums[74]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime and '0' not in str(num):
            left_truncatable = True
            for i in range(1, len(str(num))):
                if not is_prime_generator(int(str(num)[i:])):
                    left_truncatable = False
                    break
            if left_truncatable:
                primes.append(num)
    return sorted(primes)

def is_prime_generator(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True