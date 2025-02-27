def find_second_largest_num(numbers):
    if len(numbers) < 20 or not 20 <= len(numbers) <= 93:
        return None
    sub_list = numbers[19:93]
    if len(sub_list) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in sub_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None