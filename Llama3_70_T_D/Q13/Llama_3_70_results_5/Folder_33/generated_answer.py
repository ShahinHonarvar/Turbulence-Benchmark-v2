def find_second_largest_num(lst):
    slice_of_lst = lst[667:775]
    if len(slice_of_lst) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in slice_of_lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None