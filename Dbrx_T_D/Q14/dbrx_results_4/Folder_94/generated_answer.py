def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 71 - 52 or min(numbers[52:72]) == max(numbers[52:72]):
        return None
    else:
        unique_numbers = sorted(list(set(numbers[52:72])))
        if len(unique_numbers) > 1:
            return unique_numbers[1]
        else:
            return None