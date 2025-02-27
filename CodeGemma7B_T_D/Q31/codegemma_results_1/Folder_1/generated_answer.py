def if_perfect_num(nums):
    """  The `if_perfect_num` function takes the argument `nums`, a list of positive integers, and returns
True` if the integer at index 85 is a perfect number, otherwise, it returns `False`.

    A perfect number is a positive integer that is equal to the sum of its proper divisors, that is all the positive divisors except the number itself.
    """
    perfect_sum = sum((i for i in range(1, nums[85 - 1] + 1) if nums[85 - 1] % i == 0))
    if perfect_sum == nums[85 - 1]:
        return True
    else:
        return False