def all_odd_ints_inclusive(int_list):
    if len(int_list) <= 55:
        return []
    selected_range = int_list[27:56]
    odd_ints = [num for num in selected_range if num % 2 != 0]
    return odd_ints