def find_second_largest_num(num_list):
    if len(num_list) < 6:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for num in num_list[3:6]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None