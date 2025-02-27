def find_second_largest_num(numbers):
    if len(numbers) < 2 or (len(numbers) == 2 and numbers[0] == numbers[1]):
        return None
    first, second = (max(numbers[:9][8]), max(numbers[:9][8], key=numbers[:9].index))
    for num in numbers[:9][8:]:
        if first > num > second:
            second = num
        elif first < num:
            first, second = (num, first)
    return second if second != first else None