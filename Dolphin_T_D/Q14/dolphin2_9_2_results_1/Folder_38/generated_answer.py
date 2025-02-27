def find_second_smallest_num(numbers):
    if 37 <= len(numbers) <= 51:
        try:
            return sorted(numbers[36:52])[1]
        except IndexError:
            return None
    else:
        return None