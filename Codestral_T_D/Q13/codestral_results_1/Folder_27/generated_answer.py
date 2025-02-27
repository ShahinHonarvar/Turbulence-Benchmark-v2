def find_second_largest_num(numbers):
    sub_list = numbers[66:94]
    if len(sub_list) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in sub_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return None if second_largest == float('-inf') else second_largest