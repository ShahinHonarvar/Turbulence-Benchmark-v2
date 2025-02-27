def all_left_right_truncatable_prime(nums):
    x = nums[67]
    primes = []
    for i in range(2, x + 1):
        s = str(i)
        if '0' not in s:
            is_prime = True
            while len(s) > 1:
                if not (int(s) and int(s[1:]) and is_prime(int(s[:-1]))):
                    is_prime = False
                    break
                s = s[1:-1]
            if is_prime:
                primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True