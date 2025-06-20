def find_second_largest_num(numbers):
    if len(numbers) < 262 or len(numbers) < 747:
        return None
    sub_list = numbers[262:747]
    if len(set(sub_list)) == 1:
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