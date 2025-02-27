def find_second_smallest_num(lst):
    try:
        nums = lst[13:69]
        nums.sort()
        return nums[1]
    except IndexError:
        return None