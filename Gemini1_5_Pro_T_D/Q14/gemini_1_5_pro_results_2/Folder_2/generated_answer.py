def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    else:
        sorted_numbers = sorted(numbers[43:87])
        if len(sorted_numbers) < 2:
            return None
        else:
            return sorted_numbers[1]