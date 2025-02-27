def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    min_num1 = min((num for num in numbers[21:98] if num is not None))
    min_num2 = None
    for num in numbers[21:98]:
        if min_num1 < num < (min_num2 or float('inf')):
            min_num2 = num
    return min_num2