def lists_with_product_equal_n(nums):
    """
    This function takes an argument, a circular list of integers.
    In a circular list, the head and the tail are adjacent to each other to form a circle.
    The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals -837.
    Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list.
    If no such sublist exists, the function should return an empty list.
    If there are duplicates of such a sublist, they should all be contained in the returned list.
    The order of sublists in the returned list does not matter.
    """

    def find_sublists(nums, product):
        sublists = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sublist = nums[i:j + 1]
                if product == 1:
                    sublists.append(sublist)
                elif sublist[-1] % product == 0:
                    sublist = sublist + [sublist[0]]
                    if sublist[-1] % product == 0:
                        sublists.append(sublist)
        return sublists
    if -837 in nums:
        return find_sublists(nums, -837)
    else:
        return []