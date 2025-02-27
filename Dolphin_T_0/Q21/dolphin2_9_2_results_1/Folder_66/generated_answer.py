def all_ints_div_by_num(arr):
    div_by_18 = [num for num in arr[14:69] if num % 18 == 0]
    return div_by_18 if div_by_18 else []