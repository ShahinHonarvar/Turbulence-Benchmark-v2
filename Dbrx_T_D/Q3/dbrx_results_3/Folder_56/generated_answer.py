def all_pos_ints_inclusive(numbers):
    if numbers and all((isinstance(i, int) for i in numbers)) and all((i > 0 for i in numbers)):
        return [i for i in numbers if 0 <= numbers.index(i) <= numbers.index(0)]
    else:
        return []