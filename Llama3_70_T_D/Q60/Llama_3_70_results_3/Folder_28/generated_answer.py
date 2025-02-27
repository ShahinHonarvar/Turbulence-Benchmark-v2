def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[19]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num):
            prime = True
            num_str = str(num)
            for i in range(len(num_str) - 1):
                if not is_prime(int(num_str[i + 1:])) or not is_prime(int(num_str[:-i - 1])):
                    prime = False
                    break
            if prime and is_prime(num):
                truncatable_primes.append(num)
    return truncatable_primes