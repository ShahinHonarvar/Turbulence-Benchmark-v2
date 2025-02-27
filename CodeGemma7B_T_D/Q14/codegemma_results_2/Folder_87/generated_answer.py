def find_second_smallest_num(nums):
    if len(nums) == 0 or len(nums) <= 22 or len(nums) >= 89:
        return None
    nums = nums[22:89 + 1]
    num_set = set(nums)
    arr = list(num_set)
    arr.sort(reverse=False)
    if len(arr) < 2:
        return None
    return arr[1]