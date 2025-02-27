def all_left_right_truncatable_prime(nums):
    x = nums[32]
    primes = []
    for i in range(2, x + 1):
        if all((int(str(i)[j:]) > 0 and is_prime(int(str(i)[j:])) for j in range(len(str(i))))) and all((int(str(i)[:j]) > 0 and is_prime(int(str(i)[:j])) for j in range(len(str(i)), 0, -1))):
            primes.append(i)
    return primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True