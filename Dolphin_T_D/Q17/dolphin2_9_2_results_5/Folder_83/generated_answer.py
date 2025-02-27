def all_ints_div_by_both_two_nums(arr):
    result = [i for i in arr[90:201] if i % -31 == 0 and i % 13 == 0]
    return result