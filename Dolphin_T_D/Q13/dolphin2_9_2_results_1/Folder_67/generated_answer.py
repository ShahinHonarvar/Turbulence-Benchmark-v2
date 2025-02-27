def find_second_largest_num(numbers):
    if 50 < len(numbers) < 22:
        return None
    numbers = numbers[22:51]
    if len(set(numbers)) == 1:
        return None
    numbers.sort(reverse=True)
    return numbers[1]