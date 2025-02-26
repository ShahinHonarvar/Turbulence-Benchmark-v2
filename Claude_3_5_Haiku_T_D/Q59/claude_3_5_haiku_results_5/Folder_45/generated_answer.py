def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[61]
    result = []

    def is_left_truncatable_prime(num):
        num_str = str(num)
        while num_str:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[1:]
        return True
    for n in range(2, x):
        if '0' not in str(n) and is_left_truncatable_prime(n):
            result.append(n)
    return sorted(result)