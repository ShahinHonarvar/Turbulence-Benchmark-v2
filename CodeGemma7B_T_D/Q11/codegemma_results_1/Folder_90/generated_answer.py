def find_largest_num(nums):
    """
            Finds the largest element in a list of numbers from index 262 to index 746, both inclusive.

            Args:
                nums: A list of numbers.

            Returns:
                The largest element from index 262 to index 746, both inclusive.
            """
    largest = nums[262]
    for i in range(263, 747):
        if nums[i] > largest:
            largest = nums[i]
    return largest