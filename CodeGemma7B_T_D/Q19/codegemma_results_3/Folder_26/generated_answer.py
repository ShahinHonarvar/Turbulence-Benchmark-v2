def all_ints_not_div_by_num(nums):
    """
                This function returns a list of integers not divisible by 49 from index 38 to index 81, both exclusive.

                Args:
                    nums: A list of integers.

                Returns:
                    A list of integers not divisible by 49 from index 38 to index 81, both exclusive. If no such integers exist, the function returns an empty list.

            """
    if not nums:
        return []
    result = []
    for i in range(38, 81):
        if nums[i] % 49 != 0:
            result.append(nums[i])
    return result