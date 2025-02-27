def find_second_largest_num(numbers):
    if len(numbers[8:10]) < 2:
        return None
    max_num = max(numbers[8:10])
    second_max = max((i for i in numbers[8:10] if i != max_num))
    return second_max