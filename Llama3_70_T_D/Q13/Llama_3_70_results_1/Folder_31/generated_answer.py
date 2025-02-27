def find_second_largest_num(num_list):
    if len(num_list) < 89:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for num in num_list[75:89]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None