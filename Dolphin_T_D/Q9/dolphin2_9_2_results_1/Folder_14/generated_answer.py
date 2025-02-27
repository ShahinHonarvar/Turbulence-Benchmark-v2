def all_odd_ints_inclusive(input_list):
    specified_range = input_list[5:8]
    odd_ints = [int for int in specified_range if int % 2 != 0]
    return odd_ints