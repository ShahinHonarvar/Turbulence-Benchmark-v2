def all_left_right_truncatable_prime(nums):
    x = nums[85]
    primes = []
    for num in range(2, x + 1):
        if all((int(str(num)[i:]) in [2, 3, 5] or is_prime(int(str(num)[i:])) for i in range(len(str(num))))) and all((int(str(num)[:j]) in [2, 3, 5] or is_prime(int(str(num)[:j])) for j in range(1, len(str(num))))):
            primes.append(num)
    return sorted(primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True