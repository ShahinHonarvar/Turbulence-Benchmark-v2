def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 86 - 68 + 1:
        return None
    first, second = (max(numbers[68:86][0], numbers[68:86][1]), min(numbers[68:86][0], numbers[68:86][1]))
    for num in numbers[68:86][2:]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second