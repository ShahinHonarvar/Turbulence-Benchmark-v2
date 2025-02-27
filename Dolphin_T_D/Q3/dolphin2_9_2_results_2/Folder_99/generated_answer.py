def all_pos_ints_inclusive(numbers):
    result = []
    for num in numbers[310:371]:
        if num > 0:
            result.append(num)
    return result