def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 50:
        return None
    first, second = (max(numbers[35:49]), None)
    for num in numbers[35:49]:
        if num < first:
            if not second or num > second:
                second = num
    return second if second else None