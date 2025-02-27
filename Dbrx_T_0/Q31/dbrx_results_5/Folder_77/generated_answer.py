def if_perfect_num(numbers):
    if len(numbers) > 985 and numbers[984] > 0:
        num = numbers[984]
        return sum((i for i in range(1, num) if num % i == 0)) == num
    else:
        return False