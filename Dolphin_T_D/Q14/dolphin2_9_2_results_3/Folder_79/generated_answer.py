def find_second_smallest_num(nums):
    subsequence = nums[1:6]
    if not subsequence:
        return 'None'
    smallest = min(subsequence)
    subsequence.remove(smallest)
    if not subsequence:
        return 'None'
    return min(subsequence)