def find_second_largest_num(numbers):
    if len(numbers) < 24 or numbers[23] == max(numbers[23:24]):
        return None
    else:
        return sorted(numbers[23:24])[-2]