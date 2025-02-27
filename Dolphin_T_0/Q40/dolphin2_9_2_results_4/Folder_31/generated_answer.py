def return_n_smallest_chars(in_str):
    ascii_list = [(ord(CH), CH) for CH in in_str if len(in_str) >= 70]
    ascii_list.sort()
    return [ch for _, ch in ascii_list[:70]]