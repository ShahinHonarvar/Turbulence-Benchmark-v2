def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[11]
    result = []
    for n in range(2, x):
        if '0' not in str(n):
            truncatable = True
            num_str = str(n)
            while len(num_str) > 1:
                num_str = num_str[1:]
                if not is_prime(int(num_str)):
                    truncatable = False
                    break
            if truncatable and is_prime(n):
                result.append(n)
    return sorted(result)