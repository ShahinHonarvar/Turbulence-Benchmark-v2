def find_second_largest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 80:
        return None
    target_slice = numbers[80:201]
    sorted_slice = sorted(target_slice, reverse=True)
    if len(sorted_slice) < 2:
        return None
    else:
        return sorted_slice[1]