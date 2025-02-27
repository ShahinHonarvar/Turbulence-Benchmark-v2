def if_perfect_num(numbers):
    if len(numbers) > 321:
        num = numbers[321]
        return sum((factor for factor in range(1, num) if num % factor == 0)) == num
    else:
        return False