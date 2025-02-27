def find_second_largest_num(nums):
    """
            This function takes a list of distinct numbers as input and returns the second largest element from index 0 to index 1, both inclusive. If there is no such element, the function returns 'None'.
            """
    if len(nums) < 2:
        return None
    largest = nums[0]
    second_largest = None
    for num in nums[1:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and second_largest is not None:
            second_largest = num
    return second_largest