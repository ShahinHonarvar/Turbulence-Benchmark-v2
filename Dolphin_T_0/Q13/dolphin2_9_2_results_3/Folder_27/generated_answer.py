def find_second_largest_num(numbers):
    subset_numbers = numbers[66:94]
    if len(subset_numbers) < 2:
        return None
    sorted_numbers = sorted(set(subset_numbers), reverse=True)
    for num in sorted_numbers:
        if subset_numbers.count(num) > 1:
            return num
    if len(sorted_numbers) > 1:
        return sorted_numbers[1]
    else:
        return None