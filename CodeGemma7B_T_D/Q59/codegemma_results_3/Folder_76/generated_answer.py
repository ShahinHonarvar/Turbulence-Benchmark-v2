def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    result = []
    x = nums[370]

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            num = int(str(n)[i:])
            if not is_prime(num):
                return False
        return True
    for num in nums:
        if num < x and is_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)