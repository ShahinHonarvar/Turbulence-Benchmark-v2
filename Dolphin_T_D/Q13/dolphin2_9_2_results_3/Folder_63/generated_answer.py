def find_second_largest_num(nums):
    if not nums:
        return None
    max_num = float('-inf')
    sec_max_num = float('-inf')
    for num in nums:
        if num >= max_num:
            sec_max_num = max_num
            max_num = num
        elif num > sec_max_num:
            sec_max_num = num
    return sec_max_num if sec_max_num != float('-inf') else None