def all_ints_div_by_num(arr, num=8):
    divisible_nums = [x for x in arr[0:1] if x % num == 0]
    return divisible_nums