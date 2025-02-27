def all_odd_ints_exclusive(nums):
    """
    Creates a list of all odd integers from index 40 to index 200, exclusive.
    """
    answer = []
    for i in range(40, 200):
        if nums[i] % 2 == 1:
            answer.append(nums[i])
    return answer