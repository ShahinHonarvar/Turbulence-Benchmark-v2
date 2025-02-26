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
    for num in range(2, x):
        if '0' not in str(num):
            is_truncatable = True
            current = num
            while len(str(current)) > 1:
                current = int(str(current)[1:])
                if not is_prime(current):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(num):
                result.append(num)
    return sorted(result)