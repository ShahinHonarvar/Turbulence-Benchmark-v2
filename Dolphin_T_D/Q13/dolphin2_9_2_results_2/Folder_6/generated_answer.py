def find_second_largest_num(numbers):
    sublist = numbers[10:67]
    if len(sublist) < 2:
        return None
    largest = None
    second_largest = None
    for num in sublist:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or (num > second_largest and num < largest):
            second_largest = num
    return second_largest