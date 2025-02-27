def find_second_largest_num(nums):
    try:
        return sorted(nums[22:64], reverse=True)[1]
    except IndexError:
        return None