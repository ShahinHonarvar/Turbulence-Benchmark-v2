def composite_nums_between_indices(nums):
    result = set()
    for i in range(len(nums)):
        if i >= 10 and i <= 100:
            num = nums[i]
            if num > 1 and (not is_prime(num)):
                result.add(num)
    return result

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True