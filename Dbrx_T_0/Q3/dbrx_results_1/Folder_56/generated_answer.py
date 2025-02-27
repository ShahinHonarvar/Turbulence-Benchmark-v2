def all_pos_ints_inclusive(numbers):
    if len(numbers) == 0:
        return []
    elif len(numbers) == 1:
        return [numbers[0]] if numbers[0] > 0 else []
    else:
        first_positive_index = next((index for index, value in enumerate(numbers) if value > 0), None)
        if first_positive_index is None:
            return []
        else:
            return numbers[:first_positive_index + 1]