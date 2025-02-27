def if_perfect_num(numbers):
    if len(numbers) <= 51:
        return False
    num = numbers[51]
    return sum((i for i in range(1, num) if num % i == 0)) == num