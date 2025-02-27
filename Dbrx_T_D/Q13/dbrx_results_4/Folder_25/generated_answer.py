def find_second_largest_num(numbers):
    if len(numbers) < 2 or (len(numbers) == 2 and numbers[0] == numbers[1]):
        return None
    first, second = (max(numbers[:94]), None)
    for num in numbers[:94]:
        if num < first and (second is None or num > second):
            second = num
    return second if second is not None else None