def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    sub_list = numbers[:6]
    largest = float('-inf')
    second_largest = float('-inf')
    for num in sub_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None