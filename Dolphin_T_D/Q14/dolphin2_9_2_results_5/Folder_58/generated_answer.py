def find_second_smallest_num(numbers):
    if not 310 <= len(numbers) <= 370:
        return None
    numbers_sub = numbers[310:371]
    if len(numbers_sub) < 2:
        return None
    numbers_sub = list(set(numbers_sub))
    numbers_sub.sort()
    return numbers_sub[1]