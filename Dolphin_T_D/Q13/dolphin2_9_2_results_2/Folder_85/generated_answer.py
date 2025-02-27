def find_second_largest_num(numbers):
    if len(numbers) < 3:
        return None
    elif len(numbers) == 3 and len(set(numbers)) == 1:
        return None
    else:
        numbers = numbers[5:9]
        sorted_numbers = sorted(set(numbers), reverse=True)
        if len(set(numbers)) != 2:
            return None
        else:
            return sorted_numbers[1]