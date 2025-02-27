def find_second_largest_num(numbers):
    sliced_numbers = numbers[62:64]
    if len(sliced_numbers) < 2:
        return None
    else:
        sliced_numbers.sort(reverse=True)
        return sliced_numbers[1]