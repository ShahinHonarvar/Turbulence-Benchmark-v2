def find_second_largest_num(numbers):
    if len(numbers) < 751:
        return None
    sub_list = numbers[246:751]
    first_largest = second_largest = float('-inf')
    for num in sub_list:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif first_largest > num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None