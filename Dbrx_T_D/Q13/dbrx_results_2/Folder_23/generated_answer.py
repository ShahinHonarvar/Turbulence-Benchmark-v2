def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 72:
        return None
    max_num1 = max(numbers[52:72])
    max_num2 = max((x for x in numbers[52:72] if x < max_num1))
    if max_num2 == max((num for num in numbers[52:72] if num < max_num1)):
        return max_num2
    else:
        return None