def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(nums):
    x = nums[54]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            temp = num
            while temp > 9:
                temp //= 10
                if not is_prime(temp):
                    break
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)