def find_second_largest_num(nums):
    if len(nums) <= 8:
        try:
            return sorted(nums[:9])[-2]
        except IndexError:
            return None
    else:
        try:
            return sorted(nums[:9])[-2]
        except IndexError:
            return None