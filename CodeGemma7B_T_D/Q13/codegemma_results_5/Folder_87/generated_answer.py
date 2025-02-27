def find_second_largest_num(nums):
    """
            Finds the second largest number from index 36 to index 46 (inclusive) in a list of distinct numbers.

            Args:
              nums: A list of distinct numbers.

            Returns:
              The second largest number from index 36 to index 46 (inclusive), or 'None' if there is no such element.
            """
    if len(nums) < 47 or None in nums[36:47]:
        return 'None'
    second_largest = None
    largest = None
    for num in nums[36:47]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest