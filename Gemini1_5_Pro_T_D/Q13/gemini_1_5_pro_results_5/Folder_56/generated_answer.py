def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        largest = max(numbers[0], numbers[1])
        second_largest = min(numbers[0], numbers[1])
        if largest == second_largest:
            return None
        else:
            return second_largest