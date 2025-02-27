def all_odd_ints_inclusive(int_list):
    start = 59
    end = 97
    if start < 0 or end > len(int_list) - 1:
        return []
    odd_ints = [i for i in int_list[start:end + 1] if i % 2 != 0]
    return odd_ints