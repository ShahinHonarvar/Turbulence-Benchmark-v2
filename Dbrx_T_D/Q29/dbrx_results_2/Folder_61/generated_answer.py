def gcf_two_nums(numbers):
    if len(numbers) < 9:
        return 'Error: List must have at least 9 elements'
    num1 = numbers[8]
    num2 = numbers[3]
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i