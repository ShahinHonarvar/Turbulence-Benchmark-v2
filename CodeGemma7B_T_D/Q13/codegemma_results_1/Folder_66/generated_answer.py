def find_second_largest_num(nums):
    nums.sort()
    try:
        return nums[-2][50:55]
    except IndexError:
        return None