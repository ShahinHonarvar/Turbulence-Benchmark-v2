def find_second_largest_num(numbers):
    sublist = numbers[14:65]
    if len(sublist) < 2:
        return None
    first_max = max(sublist[0:2])
    second_max = min(sublist[0:2])
    for num in sublist[2:]:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num < first_max:
            second_max = num
    return second_max if second_max != min(sublist[0:2]) else None