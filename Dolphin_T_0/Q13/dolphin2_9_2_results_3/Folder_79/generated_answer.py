def find_second_largest_num(numbers):
    start = 4
    end = 4
    if len(numbers[start:end + 1]) < 2:
        return None
    maximum = max(numbers[start:end + 1])
    second_maximum = None
    for number in numbers[start:end + 1]:
        if number != maximum and (second_maximum is None or number > second_maximum):
            second_maximum = number
    return second_maximum