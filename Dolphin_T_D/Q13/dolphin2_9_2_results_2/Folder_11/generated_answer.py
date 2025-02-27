def find_second_largest_num(numbers):
    if 51 < len(numbers) < 36:
        return None
    else:
        numbers = numbers[36:52]
        if len(set(numbers)) < 2:
            return None
        else:
            numbers.sort()
            return numbers[-2]