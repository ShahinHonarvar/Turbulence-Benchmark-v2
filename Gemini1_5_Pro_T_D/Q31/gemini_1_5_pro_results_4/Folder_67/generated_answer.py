def if_perfect_num(numbers):
    if len(numbers) <= 43:
        return False
    num = numbers[43]
    sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i + num // i
    if sum == num:
        return True
    else:
        return False