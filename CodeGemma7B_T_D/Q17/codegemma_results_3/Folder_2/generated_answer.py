def all_ints_div_by_both_two_nums(nums: List[int]) -> List[int]:
    """
            Return the list of integers in given list divisible by both 54 and 82 from index 73 to index 86, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
            """
    result = []
    for num in nums[73:87]:
        if num % 54 == 0 and num % 82 == 0:
            result.append(num)
    return result