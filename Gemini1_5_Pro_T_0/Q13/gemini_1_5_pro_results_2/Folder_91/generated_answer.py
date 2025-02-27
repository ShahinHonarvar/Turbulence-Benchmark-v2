def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 7:
        return None
    sub_numbers = numbers[:6]
    largest = max(sub_numbers)
    second_largest = min(sub_numbers)
    for i in range(len(sub_numbers)):
        if sub_numbers[i] != largest and sub_numbers[i] > second_largest:
            second_largest = sub_numbers[i]
    if second_largest == largest:
        return None
    else:
        return second_largest