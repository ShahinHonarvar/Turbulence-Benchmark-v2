def all_pos_ints_inclusive(numbers):
    output = []
    for number in numbers:
        if number > 0 and 19 <= number <= 92:
            output.append(number)
    return output