def all_ints_div_by_num(arr):
    divisible_by_num_list = [x for x in arr[18:39] if x % -97 == 0]
    return divisible_by_num_list if len(divisible_by_num_list) > 0 else []