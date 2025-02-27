def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 605 - 533 + 1:
        return None
    first, second = (max(numbers[533:605]), None)
    for num in numbers[533:605]:
        if num < first:
            if second is None or num > second:
                second = num
    return second