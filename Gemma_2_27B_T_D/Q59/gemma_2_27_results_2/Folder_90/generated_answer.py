def all_left_truncatable_prime(nums):
    x = nums[466]
    primes = []
    for num in range(x, 1, -1):
        prime = True
        n = str(num)
        if '0' in n:
            continue
        for i in range(len(n)):
            if not is_prime(int(n[:len(n) - i])):
                prime = False
                break
        if prime:
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True