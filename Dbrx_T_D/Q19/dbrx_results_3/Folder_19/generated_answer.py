def all_ints_not_div_by_num(nums):
    if not nums or not isinstance(nums, list):
        return []
    sub_list = nums[4:5]
    result = [n for n in sub_list if n % -7 != 0]
    return result