def all_ints_div_by_both_two_nums(arr):
    range_list = arr[1:5]
    result = [i for i in range_list if i % 4 == 0 and i % -6 == 0]
    return result