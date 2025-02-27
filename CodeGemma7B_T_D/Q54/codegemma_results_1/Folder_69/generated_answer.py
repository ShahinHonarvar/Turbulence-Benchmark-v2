def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_primes(nums):
    result = []
    for num in nums:
        if is_prime(num):
            copy = num
            while copy > 0:
                if not is_prime(copy):
                    break
                copy //= 10
            else:
                result.append(num)
    return sorted(result, reverse=True)