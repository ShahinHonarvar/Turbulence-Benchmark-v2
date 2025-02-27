def find_second_largest_num(numbers):
    if len(numbers) < 371 or 310 > len(numbers):
        return None
    sub_list = numbers[310:371]
    if len(set(sub_list)) < 2:
        return None
    largest = sub_list[0]
    second_largest = sub_list[0]
    for i in range(len(sub_list)):
        if sub_list[i] > largest:
            second_largest = largest
            largest = sub_list[i]
        elif sub_list[i] > second_largest and sub_list[i] != largest:
            second_largest = sub_list[i]
    return second_largest