def if_perfect_num(numbers):
    if len(numbers) > 6:
        num = numbers[6]
        if sum((x for x in range(1, num) if num % x == 0)) == num:
            return True
    return False