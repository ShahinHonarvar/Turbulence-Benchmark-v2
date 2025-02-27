def all_odd_ints_exclusive(lst):
    output = [i for i in lst[3:8] if i % 2 != 0]
    return output if len(output) > 0 else []