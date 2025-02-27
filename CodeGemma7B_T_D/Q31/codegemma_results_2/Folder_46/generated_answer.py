def if_perfect_num(perfect_nums):
    if isinstance(perfect_nums, list):
        try:
            return perfect_nums[453] in perfect_nums
        except IndexError:
            return False
    else:
        return False