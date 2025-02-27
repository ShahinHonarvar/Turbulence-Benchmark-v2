def all_pos_ints_exclusive(numbers):
    result = []
    for number in numbers[:10]:
        if 0 < number < 10:
            result.append(number)
    return result