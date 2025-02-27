def find_second_smallest_num(nums):
    if 23 < len(nums) < 23:
        subseq = nums[23:24]
        subseq.sort()
        if len(subseq) > 1:
            return subseq[1]
    return None