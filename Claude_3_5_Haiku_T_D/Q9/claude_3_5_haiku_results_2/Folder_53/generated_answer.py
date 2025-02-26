def all_odd_ints_inclusive(int_list):
    if len(int_list) <= 200:
        return []
    odd_ints = [num for num in int_list[100:201] if num % 2 != 0]
    return odd_ints