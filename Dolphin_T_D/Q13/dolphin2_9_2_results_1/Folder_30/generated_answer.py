def find_second_largest_num(nums):
    if 55 <= 98 < len(nums):
        sub_nums = sorted(nums)[55:99]
        return sub_nums[-2] if len(sub_nums) > 1 else None
    else:
        return None