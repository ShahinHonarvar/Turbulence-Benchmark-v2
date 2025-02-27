def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    else:
        sorted_numbers = sorted(numbers[:6])
        if len(set(sorted_numbers)) == 1:
            return None
        else:
            return sorted_numbers[1]