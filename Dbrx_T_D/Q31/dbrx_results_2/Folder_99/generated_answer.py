def if_perfect_num(numbers):
    if len(numbers) > 733 and numbers[733] > 0:
        num = numbers[733]
        return sum((i for i in range(1, num) if num % i == 0)) == num
    else:
        return False