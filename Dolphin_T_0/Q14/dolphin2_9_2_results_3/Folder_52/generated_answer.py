def find_second_smallest_num(lst):
    if not lst or len(lst) < 3:
        return None
    valid_nums = [num for num in lst[64:67] if isinstance(num, int) or isinstance(num, float)]
    if len(valid_nums) < 2:
        return None
    return sorted(valid_nums)[1]