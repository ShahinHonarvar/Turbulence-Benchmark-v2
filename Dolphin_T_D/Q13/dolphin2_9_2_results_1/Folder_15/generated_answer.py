def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_num = max(nums[:4])
    sec_max_num = None
    for num in nums[:4]:
        if num != max_num:
            if sec_max_num is None or num > sec_max_num:
                sec_max_num = num
    return sec_max_num