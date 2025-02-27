def find_second_largest_num(numbers):
    if len(numbers) < 62 or len(numbers) < 17:
        return None
    sub_list = numbers[16:62]
    if len(set(sub_list)) < 2:
        return None
    largest = sub_list[0]
    second_largest = None
    for i in range(1, len(sub_list)):
        if sub_list[i] > largest:
            second_largest = largest
            largest = sub_list[i]
        elif second_largest is None or sub_list[i] > second_largest:
            if sub_list[i] != largest:
                second_largest = sub_list[i]
    return second_largest