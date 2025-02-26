def find_second_largest_num(numbers):
    if len(numbers) < 30:
        return None
    sub_list = numbers[29:94]
    if len(sub_list) < 2:
        return None
    largest = float('-inf')
    second_largest = float('-inf')
    for num in sub_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None