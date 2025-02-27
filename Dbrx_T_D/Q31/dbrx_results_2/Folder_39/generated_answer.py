def if_perfect_num(numbers):
    if len(numbers) > 59 and numbers[59] > 0:
        num = numbers[59]
        return sum((i for i in range(1, num) if num % i == 0)) == num
    else:
        return False