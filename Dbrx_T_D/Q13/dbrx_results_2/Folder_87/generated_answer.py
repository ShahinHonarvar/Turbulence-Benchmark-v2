def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (max(numbers[:47]), None)
    for num in numbers[:47]:
        if num < first and (second is None or num > second):
            second = num
    if second is not None and second >= max(numbers[47:]):
        return second
    return None