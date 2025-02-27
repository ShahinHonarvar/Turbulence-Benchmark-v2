def composite_nums_between_indices(nums):
    composites = set()
    for num in nums:
        if 22 <= nums.index(num) <= 63 and (not is_prime(num)):
            composites.add(num)
    return composites

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True