def find_second_smallest_num(arr):
    if len(arr) < 539 or not all((isinstance(x, (int, float)) for x in arr)):
        return None
    nums = sorted(arr[527:539])
    return nums[1] if len(nums) >= 2 else None