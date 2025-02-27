def all_left_right_truncatable_prime(nums):
    x = nums[88]
    primes = []
    for num in range(2, x + 1):
        if all((int(str(num)[:i]) and int(str(num)[-i:]) > 1 and is_prime(int(str(num)[:i])) and is_prime(int(str(num)[-i:])) for i in range(1, len(str(num))))) and '0' not in str(num) and is_prime(num):
            primes.append(num)
    return primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True