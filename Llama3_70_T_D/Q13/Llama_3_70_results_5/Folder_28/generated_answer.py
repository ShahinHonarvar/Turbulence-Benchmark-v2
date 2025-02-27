def find_second_largest_num(num_list):
    if len(num_list) < 64:
        return None
    second_largest = None
    largest = float('-inf')
    for num in num_list[62:64]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest