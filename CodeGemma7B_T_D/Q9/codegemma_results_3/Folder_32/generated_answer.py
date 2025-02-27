def all_odd_ints_inclusive(nums):
    """
    Args:
        nums: A list of integers.

    Returns:
        A list of all odd integers from index 21 to index 97, both inclusive, in the input list. If no odd integers exist in the specified range, an empty list is returned.
    """
    try:
        first_odd = next((i for i in nums[20:97 + 1] if i % 2 != 0))
    except StopIteration:
        return []
    result = []
    for i in range(first_odd, 98, 2):
        result.append(i)
    return result