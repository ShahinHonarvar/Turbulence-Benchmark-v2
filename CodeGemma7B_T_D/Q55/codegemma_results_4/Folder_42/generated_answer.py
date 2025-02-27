def lists_with_product_equal_n(nums):
    """
    This function takes a circular list of integers and returns a list of sublists each of which contains the contiguous integers from the given list such that their product equals 25.
    Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list.
    If no such sublist exists, the function should return an empty list.
    If there are duplicates of such a sublist, they should all be contained in the returned list.
    The order of sublists in the returned list does not matter.
    """
    results = []
    for i in range(len(nums)):
        nums.append(nums.pop(0))
        i = 0
        product = 1
        for j in range(i, len(nums)):
            if product == 25:
                results.append(nums[i:j + 1])
                product = 1
                i = j + 1
            elif product > 25:
                product //= nums[i]
                i += 1
            else:
                product *= nums[j]
    return results