def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (max(numbers[91:100], default=None), None)
    for num in numbers[91:100]:
        if num < first:
            second = first
            first = num
        elif num > second and num < first:
            second = num
    return second