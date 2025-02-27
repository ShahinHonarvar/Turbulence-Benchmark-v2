def find_second_smallest_num(nums):
    if not 22 <= len(nums) >= 63:
        return None
    sub_list = nums[22:64]
    sub_list.sort()
    if len(set(sub_list)) == 1:
        return None
    for num in sub_list:
        if sub_list.count(num) > 1 and num != min(sub_list):
            return num
    return None