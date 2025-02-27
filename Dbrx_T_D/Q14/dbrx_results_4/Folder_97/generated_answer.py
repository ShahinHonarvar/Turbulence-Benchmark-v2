def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[31:35]) < 2:
        return None
    min_num1, min_num2 = (min(numbers[31:35]), max(numbers[31:35]))
    for num in numbers[31:35]:
        if num < min_num1:
            min_num1, min_num2 = (num, min_num1)
        elif min_num1 < num < min_num2:
            min_num2 = num
    if min_num2 == max(numbers[31:35]):
        return None
    return min_num2