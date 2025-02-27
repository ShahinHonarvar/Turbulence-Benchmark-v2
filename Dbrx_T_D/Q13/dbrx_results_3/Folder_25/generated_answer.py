def find_second_largest_num(numbers):
    if len(numbers) < 2 or (len(numbers) == 2 and numbers[0] == numbers[1]):
        return None
    first, second = (max(numbers[:94][29:]), max(numbers[28:94]))
    if first == second:
        second = max(numbers[28:], key=lambda x: (x < first, x))
    return second