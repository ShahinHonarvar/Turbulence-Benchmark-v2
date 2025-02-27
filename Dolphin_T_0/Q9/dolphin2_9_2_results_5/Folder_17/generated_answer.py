def all_odd_ints_inclusive(lst):
    valid_indices = list(range(62, 79))
    odd_ints = [num for num in lst if num % 2 != 0 and lst.index(num) in valid_indices]
    return odd_ints if len(odd_ints) > 0 else []