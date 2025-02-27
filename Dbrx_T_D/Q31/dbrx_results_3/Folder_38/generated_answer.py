def if_perfect_num(numbers):
    if len(numbers) > 38:
        num = numbers[38]
        return num > 0 and 1 + sum((j for i in range(2, int(num ** 0.5) + 1) for j in (i, num // i) if num % i == 0)) == num
    else:
        return False