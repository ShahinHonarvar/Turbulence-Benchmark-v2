def all_right_truncatable_prime(nums):
    x = nums[29]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            i_str = str(i)
            is_right_truncatable = True
            for j in range(1, len(i_str)):
                if not is_prime(int(i_str[:-j])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True