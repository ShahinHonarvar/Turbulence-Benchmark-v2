def if_perfect_num(numbers):
    perfect_num = lambda num: sum((x for x in range(1, num) if num % x == 0)) == num
    return perfect_num(numbers[701]) if len(numbers) > 701 else False