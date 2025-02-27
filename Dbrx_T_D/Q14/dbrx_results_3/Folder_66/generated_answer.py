def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 38 or len(numbers[62:100]) < 2:
        return None
    min_num1 = min(numbers[62:100])
    numbers.remove(min_num1)
    min_num2 = min(numbers[62:100])
    numbers.append(min_num1)
    if min_num2 == min_num1:
        return None
    else:
        return min_num2