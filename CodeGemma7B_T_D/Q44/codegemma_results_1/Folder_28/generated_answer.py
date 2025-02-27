def composite_nums_between_indices(nums):
    composites = set()
    for i in range(22, 89):
        if nums[i] > 1 and (not is_prime(nums[i])):
            composites.add(nums[i])
    return composites

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True