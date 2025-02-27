def find_second_largest_num(numbers):
    if len(numbers) <= 6:
        return None
    single_element = [numbers[6]]
    single_element.sort(reverse=True)
    return single_element[0] if len(single_element) > 1 else None