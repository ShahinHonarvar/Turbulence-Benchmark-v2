def if_perfect_num(numbers):
    if len(numbers) > 87 and numbers[87] > 0:
        num = numbers[87]
        return sum((i for i in range(1, num) if num % i == 0)) == num
    else:
        return False