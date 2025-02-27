def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 35 or len(numbers) > 1000:
        return None
    first, second = (max(numbers[:35]), None)
    for num in numbers[:35]:
        if num < first and (second is None or num > second):
            second = num
    return second