def all_odd_ints_inclusive(input_list):
    if len(input_list) < 200:
        return []
    odd_ints = [i for i in input_list[100:201] if i % 2 != 0]
    return odd_ints