def all_pos_ints_inclusive(numbers):
    result = []
    for num in numbers[209:557]:
        if num > 0:
            result.append(num)
    return result if result else []