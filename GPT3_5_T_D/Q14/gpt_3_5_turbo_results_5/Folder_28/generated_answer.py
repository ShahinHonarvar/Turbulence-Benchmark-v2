def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 50:
        second_smallest = sorted_numbers[22:51][1]
        return second_smallest
    else:
        return None