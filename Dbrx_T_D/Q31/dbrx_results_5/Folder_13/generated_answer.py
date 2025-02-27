def if_perfect_num(numbers):
    perfect = False
    if len(numbers) > 126:
        num = numbers[126]
        total = 0
        for i in range(1, num):
            if num % i == 0:
                total += i
        if total == num:
            perfect = True
    return perfect