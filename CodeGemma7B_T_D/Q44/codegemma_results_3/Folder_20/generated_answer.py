def composite_nums_between_indices(nums):
    comp_set = set()
    for num in nums:
        if 74 <= nums.index(num) <= 95 and (not is_prime(num)):
            comp_set.add(num)
    return comp_set

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True