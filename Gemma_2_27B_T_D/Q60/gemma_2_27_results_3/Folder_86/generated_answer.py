def all_left_right_truncatable_prime(nums):
    x = nums[126]
    primes = []
    for i in range(2, x + 1):
        if all((int(str(i)[:j]) > 1 and is_prime(int(str(i)[:j])) for j in range(1, len(str(i)) + 1))) and all((int(str(i)[j:]) > 1 and is_prime(int(str(i)[j:])) for j in range(len(str(i))))):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True