def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums:
        if num > 1 and (not is_prime(num)):
            if 0 <= nums.index(num) <= 4:
                composite_nums.add(num)
    return composite_nums

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True