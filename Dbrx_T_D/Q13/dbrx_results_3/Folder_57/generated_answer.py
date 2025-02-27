def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 55 - 27:
        return None
    first, second = (max(numbers[27:56]), None)
    for num in numbers[27:56]:
        if num < first:
            if not second or num > second:
                second = num
    return second