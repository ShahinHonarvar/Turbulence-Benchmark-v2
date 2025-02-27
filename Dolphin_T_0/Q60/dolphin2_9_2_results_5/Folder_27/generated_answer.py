def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[79]
    primes = []
    for num in range(x, 1, -1):
        truncations = [int(str(num)[1:-1])]
        while len(truncations[-1]) > 2:
            truncations.append(int(str(truncations[-1])[1:-1]))
        if all((is_prime(i) for i in truncations[::-1] + truncations)):
            primes.append(num)
    return primes