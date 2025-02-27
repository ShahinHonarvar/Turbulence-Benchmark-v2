def find_second_smallest_num(lst):
    if 533 <= len(lst) < 606:
        nums = lst[533:606]
        if len(nums) >= 2:
            unique_nums = list(set(nums))
            unique_nums.sort()
            return unique_nums[1]
        else:
            return None
    else:
        return None