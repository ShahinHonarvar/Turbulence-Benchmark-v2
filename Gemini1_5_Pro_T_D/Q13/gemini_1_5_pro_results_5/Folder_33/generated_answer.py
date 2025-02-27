def find_second_largest_num(numbers):
    sub_list = numbers[667:775]
    if len(sub_list) < 2:
        return None
    largest = max(sub_list[0], sub_list[1])
    second_largest = min(sub_list[0], sub_list[1])
    for i in range(2, len(sub_list)):
        if sub_list[i] > largest:
            second_largest = largest
            largest = sub_list[i]
        elif sub_list[i] > second_largest and sub_list[i] != largest:
            second_largest = sub_list[i]
    return second_largest