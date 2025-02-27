def if_perfect_num(numbers):
    if len(numbers) < 3:
        return False
    num = numbers[2]
    return num > 0 and sum((i for i in range(1, num) if num % i == 0)) == num