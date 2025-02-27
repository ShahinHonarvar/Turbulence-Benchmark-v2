def all_neg_ints_exclusive(nums):
    """Creates a new list by extracting negative integers from a specified range from the argument list.

          Args:
            nums: A list of integers.

          Returns:
            A list of specific negative integers from index 28 to index 49, exclusive. If no such integers exist, an empty list is returned.
          """
    answer = []
    for i in range(28, 49):
        if nums[i] < 0:
            answer.append(nums[i])
    return answer