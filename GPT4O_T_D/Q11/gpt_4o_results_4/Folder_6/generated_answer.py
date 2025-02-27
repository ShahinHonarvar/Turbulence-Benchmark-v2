def find_largest_num(numbers):
    if len(numbers) < 67:
        return None
    sub_array = numbers[10:67]
    largest_element = max(sub_array)
    return largest_element