def find_second_smallest_num(lst):
    sublst = lst[75:86]
    nums = set(sublst)
    if len(nums) < 2:
        return None
    return sorted(nums)[1]