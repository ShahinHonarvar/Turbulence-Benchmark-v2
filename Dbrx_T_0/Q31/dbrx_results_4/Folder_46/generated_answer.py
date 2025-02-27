def if_perfect_num(numbers):
    if len(numbers) > 453 and numbers[453] > 0:
        num = numbers[453]
        return sum((i for i in range(1, num) if num % i == 0)) == num
    else:
        return False