def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    else:
        sorted_numbers = sorted(numbers[:9])
        if len(sorted_numbers) == len(set(sorted_numbers)):
            return sorted_numbers[1]
        else:
            return None