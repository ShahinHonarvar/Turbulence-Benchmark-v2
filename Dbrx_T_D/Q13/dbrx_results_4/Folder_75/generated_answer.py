def find_second_largest_num(numbers):
    if len(numbers) < 2 or (len(numbers) == 2 and numbers[0] == numbers[1]):
        return None
    first, second = (max(numbers[:57] + numbers[56:]), max(numbers[:56]))
    if first == second:
        return None
    return second