def all_pos_ints_inclusive(numbers):
    if len(numbers) < 35 or not numbers[30:35].isdecimal():
        return []
    else:
        return [int(x) for x in numbers[30:35] if int(x) > 0]