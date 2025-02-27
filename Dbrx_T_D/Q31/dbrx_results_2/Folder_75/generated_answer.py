def if_perfect_num(numbers):
    if len(numbers) > 80:
        num = numbers[80]
        return num > 0 and sum((i for i in range(1, num) if num % i == 0)) == num
    else:
        return False