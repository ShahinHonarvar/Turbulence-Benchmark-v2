def find_second_smallest_num(nums):
    subarray = nums[42:69]
    if len(subarray) < 2:
        return None
    else:
        subarray.sort()
        for i in range(1, len(subarray)):
            if subarray[i] != subarray[i - 1]:
                return subarray[i]
        return None