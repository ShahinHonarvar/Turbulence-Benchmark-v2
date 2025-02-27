def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 200 <= 40:
        return None
    first, second = (max(numbers[40:200]), None)
    for num in numbers[40:200]:
        if num >= first:
            continue
        if second is None or num > second:
            second = num
    return second