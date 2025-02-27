def find_second_largest_num(numbers):
    if len(numbers) < 2 or (len(numbers) == 2 and numbers[0] == numbers[1]):
        return None
    first, second = (max(numbers[56:58]), max(numbers[:56] + numbers[58:]))
    if first > second:
        first, second = (second, first)
    return second if first != second else None