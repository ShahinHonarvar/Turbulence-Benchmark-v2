def find_second_largest_num(nums):
    try:
        temp = sorted(nums[32:36], reverse=True)
        return temp[1]
    except IndexError:
        return None