def find_second_largest_num(nums):
    nums.sort(reverse=True)
    try:
        return nums[70:85][1]
    except IndexError:
        return None