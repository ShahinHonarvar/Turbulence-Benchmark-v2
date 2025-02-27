def if_perfect_num(numbers):
    if len(numbers) > 38:
        num = numbers[38]
        return sum((i for i in range(1, num) if num % i == 0)) == num
    else:
        return False