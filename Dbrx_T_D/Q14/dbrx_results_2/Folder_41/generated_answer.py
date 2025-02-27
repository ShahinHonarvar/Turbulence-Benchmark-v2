def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    min_num1 = min(numbers[4:5])
    min_num2 = float('inf')
    count = 0
    for num in numbers[4:5]:
        if num == min_num1:
            continue
        if num < min_num2:
            min_num2 = num
            count += 1
    if count == 0:
        return None
    else:
        return min_num2