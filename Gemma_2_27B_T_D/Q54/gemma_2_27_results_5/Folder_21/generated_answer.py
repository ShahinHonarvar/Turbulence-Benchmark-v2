def all_right_truncatable_prime(nums):
    x = nums[175]
    primes = []
    for num in range(2, x):
        is_prime = True
        prime_str = str(num)
        while len(prime_str) > 0:
            if not is_prime_number(int(prime_str)):
                is_prime = False
                break
            prime_str = prime_str[:-1]
        if is_prime:
            primes.append(num)
    return sorted(primes)

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True