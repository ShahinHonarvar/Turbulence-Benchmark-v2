def find_second_smallest_num(numbers):
    if len(numbers) < 31:
        return None
    min_num1 = min(numbers[20:31])
    min_num2 = None
    for num in numbers[20:31]:
        if num > min_num1:
            min_num2 = min(min_num2, num) if min_num2 else num
    return min_num2