def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    sublist = numbers[4:9]
    if len(sublist) < 2:
        return None
    first, second = (max(sublist[0], sublist[1]), min(sublist[0], sublist[1]))
    for num in sublist[2:]:
        if num > first:
            first, second = (num, first)
        elif num > second and num != first:
            second = num
    return second if second != first else None