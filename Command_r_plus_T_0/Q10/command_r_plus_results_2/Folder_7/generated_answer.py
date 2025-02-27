def all_odd_ints_exclusive(int_list):
    odd_range = [num for i, num in enumerate(int_list[323:973], 323) if num % 2 != 0]
    return odd_range