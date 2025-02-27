def find_second_largest_num(numbers):
    if len(numbers) < 12:
        return None
    sub_numbers = numbers[10:101]
    if len(sub_numbers) == 1:
        return None
    largest = max(sub_numbers[0], sub_numbers[1])
    second_largest = min(sub_numbers[0], sub_numbers[1])
    for i in range(2, len(sub_numbers)):
        if sub_numbers[i] > largest:
            second_largest = largest
            largest = sub_numbers[i]
        elif sub_numbers[i] > second_largest and sub_numbers[i] != largest:
            second_largest = sub_numbers[i]
    return second_largest