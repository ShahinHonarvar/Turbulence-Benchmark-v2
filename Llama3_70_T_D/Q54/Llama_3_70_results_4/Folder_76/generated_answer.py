def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(nums):
    x = nums[370]
    truncatable_primes = set()
    for i in range(2, x):
        str_i = str(i)
        prime = True
        for j in range(len(str_i), 0, -1):
            if not is_prime(int(str_i[:j])):
                prime = False
                break
        if prime:
            truncatable_primes.add(i)
    return sorted(list(truncatable_primes), reverse=True)