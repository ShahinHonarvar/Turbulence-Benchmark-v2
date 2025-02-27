def if_perfect_num(numbers):
    if len(numbers) > 222:
        num = numbers[222]
        return sum([x for x in range(1, num) if num % x == 0]) == num
    else:
        return False