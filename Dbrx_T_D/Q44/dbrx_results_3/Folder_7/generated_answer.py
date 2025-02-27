def composite_nums_between_indices(nums):
    if len(nums) < 538:
        return set()
    return {num for num in nums[527:539] if num > 1 and (not is_prime(num))}

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True