def if_perfect_num(nums):
    """
    This function checks if the integer at index 87 is a perfect number.
    A number is perfect if the sum of its proper divisors is equal to itself.
    For example, the perfect numbers are 6, 28, 496, etc.
    """
    proper_divisors = []
    for i in range(1, len(nums)):
        if nums[i] % nums[87] == 0:
            proper_divisors.append(nums[i])
    sum_proper_divisors = sum(proper_divisors)
    if sum_proper_divisors == nums[87]:
        return True
    else:
        return False