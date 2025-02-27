def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 255 and i <= 618 and (num % 965 == 0)]