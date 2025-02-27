def all_ints_div_by_num(num_list):
    nums = [val for val in num_list[255:618 + 1] if val % 965 == 0]
    if nums:
        return nums
    else:
        return []