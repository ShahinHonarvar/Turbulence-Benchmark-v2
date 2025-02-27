def find_second_largest_num(numbers):
    if len(numbers) < 56:
        return None
    sub_list = numbers[34:56]
    if len(sub_list) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in sub_list:
        if num > largest:
            second_largest, largest = (largest, num)
        elif second_largest < num < largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None