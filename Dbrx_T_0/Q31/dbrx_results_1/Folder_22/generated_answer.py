def if_perfect_num(numbers):
    if len(numbers) > 72:
        num = numbers[72]
        return sum((i for i in range(1, num) if num % i == 0)) == num
    else:
        return False