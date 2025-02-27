def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    sub_list = numbers[68:87]
    if len(sub_list) < 2:
        return None
    first_largest = second_largest = float('-inf')
    for num in sub_list:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num != first_largest:
            second_largest = num
    return None if second_largest == float('-inf') else second_largest