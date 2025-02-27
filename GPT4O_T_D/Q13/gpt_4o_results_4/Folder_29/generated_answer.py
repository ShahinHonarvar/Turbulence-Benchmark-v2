def find_second_largest_num(numbers):
    if len(numbers) < 98:
        return None
    sub_list = numbers[59:98]
    if len(sub_list) < 2:
        return None
    largest = float('-inf')
    second_largest = float('-inf')
    for num in sub_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest