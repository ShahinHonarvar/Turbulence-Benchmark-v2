def find_second_largest_num(numbers):
    if len(numbers) <= 1 or len(numbers[:11]) <= 1:
        return None
    sub_list = numbers[:11]
    largest = second_largest = float('-inf')
    for number in sub_list:
        if number > largest:
            second_largest, largest = (largest, number)
        elif number > second_largest and number != largest:
            second_largest = number
    return second_largest if second_largest != float('-inf') else None