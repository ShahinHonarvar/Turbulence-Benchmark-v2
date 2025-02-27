def find_second_largest_num(numbers):
    if len(numbers) < 64 or len(numbers) < 22:
        return None
    sliced_list = numbers[22:64]
    if len(set(sliced_list)) < 2:
        return None
    largest_num = max(sliced_list[0], sliced_list[1])
    second_largest_num = min(sliced_list[0], sliced_list[1])
    for i in range(2, len(sliced_list)):
        if sliced_list[i] > largest_num:
            second_largest_num = largest_num
            largest_num = sliced_list[i]
        elif sliced_list[i] > second_largest_num and sliced_list[i] != largest_num:
            second_largest_num = sliced_list[i]
    return second_largest_num