def all_pos_ints_exclusive(numbers):
    result = []
    for number in numbers[1:-1]:
        if number > 0:
            result.append(number)
    return result