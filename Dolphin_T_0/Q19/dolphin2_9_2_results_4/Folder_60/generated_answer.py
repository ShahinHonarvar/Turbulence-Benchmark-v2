def all_ints_not_div_by_num(numbers, divisor=-99):
    range_start = 63
    range_end = 73
    filtered_numbers = [num for num in numbers[range_start:range_end] if num % divisor != 0]
    if not filtered_numbers:
        return []
    return filtered_numbers