def find_second_largest_num(lst):
    if 533 <= len(lst) <= 605:
        distinct_nums = list(set(lst[533:606]))
        if len(distinct_nums) >= 2:
            distinct_nums.sort()
            return distinct_nums[-2]
    return None