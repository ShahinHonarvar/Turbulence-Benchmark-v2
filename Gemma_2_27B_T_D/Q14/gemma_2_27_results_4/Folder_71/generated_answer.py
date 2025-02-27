def find_second_smallest_num(nums):
    try:
        sub_list = nums[29:52]
        sorted_list = sorted(sub_list)
        return sorted_list[1]
    except:
        return None