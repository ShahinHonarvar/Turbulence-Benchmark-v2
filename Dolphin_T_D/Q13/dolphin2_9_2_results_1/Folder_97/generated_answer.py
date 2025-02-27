def find_second_largest_num(nums):
    if 40 <= len(nums) <= 80:
        new_nums = nums[40:81]
        if len(set(new_nums)) < 2:
            return None
        else:
            return sorted(set(new_nums))[-2]
    else:
        return None