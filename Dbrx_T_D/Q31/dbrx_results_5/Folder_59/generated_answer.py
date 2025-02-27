def if_perfect_num(numbers):
    if len(numbers) >= 3:
        num = numbers[2]
        return sum((x for x in range(1, num) if num % x == 0)) == num
    else:
        return False