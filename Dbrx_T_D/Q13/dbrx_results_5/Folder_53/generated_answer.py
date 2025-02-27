def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 200:
        return None
    first_part = numbers[100:201]
    first_part.sort(reverse=True)
    if len(first_part) < 2:
        return None
    return first_part[1]