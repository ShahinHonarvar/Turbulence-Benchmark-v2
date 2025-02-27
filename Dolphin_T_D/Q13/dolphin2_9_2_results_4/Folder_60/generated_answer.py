def find_second_largest_num(lst):
    if 75 <= len(lst) <= 85:
        sorted_nums = sorted(lst, reverse=True)
        for num in sorted_nums:
            if num != max(lst):
                return num
    else:
        return None