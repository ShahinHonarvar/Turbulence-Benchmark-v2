def find_second_largest_num(num_list):
    if len(num_list) < 2 or len(num_list) < 371 - 310 + 1:
        return None
    num_list = num_list[310:371]
    first_largest = second_largest = float('-inf')
    for num in num_list:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif second_largest < num < first_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None