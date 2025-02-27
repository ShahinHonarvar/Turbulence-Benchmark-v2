def find_second_largest_num(numbers):
    if len(numbers) < 3 or not 6 <= numbers[0] <= numbers[1] <= numbers[2] <= 8:
        return None
    first_part = sorted(numbers[6:9])
    second_part = sorted(numbers[:6] + numbers[9:])
    combined = first_part + second_part
    if len(combined) < 2:
        return None
    return combined[-2]