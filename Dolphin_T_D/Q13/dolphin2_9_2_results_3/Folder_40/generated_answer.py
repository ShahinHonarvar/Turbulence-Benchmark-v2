def find_second_largest_num(numbers):
    first = max(numbers[0], numbers[1], numbers[2])
    second = None
    for num in numbers:
        if num != first and (second is None or num > second):
            second = num
    return second