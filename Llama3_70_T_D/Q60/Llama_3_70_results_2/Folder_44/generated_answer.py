def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[39]
    primes = []
    for i in range(2, x + 1):
        if '0' not in str(i) and is_prime(i):
            temp = str(i)
            while len(temp) > 2:
                temp = temp[1:-1]
                if not is_prime(int(temp)):
                    break
            else:
                primes.append(i)
    return sorted(primes)