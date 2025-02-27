def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 201 or len(numbers) > 1000:
        return None
    min_num1 = min(numbers[70:200])
    numbers.remove(min_num1)
    min_num2 = min(numbers[70:200])
    numbers.add(min_num1)
    if min_num1 == min_num2:
        return None
    else:
        return min_num2