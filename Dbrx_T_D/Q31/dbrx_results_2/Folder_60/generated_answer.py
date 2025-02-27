def if_perfect_num(numbers):
    if len(numbers) > 88:
        num = numbers[88]
        return num > 0 and sum((i for i in range(1, num) if num % i == 0)) == num
    else:
        return False