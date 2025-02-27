def if_perfect_num(perfect_nums):
    if perfect_nums[43] % 2 != 0 and perfect_nums[43] % 3 != 0 and (perfect_nums[43] % 5 != 0):
        return True
    else:
        return False