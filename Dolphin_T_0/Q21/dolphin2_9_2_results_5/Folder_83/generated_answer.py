def all_ints_div_by_num(arr):
    result = [num for num in arr[40:401] if num % 7 == 0]
    if result:
        return result
    else:
        return []