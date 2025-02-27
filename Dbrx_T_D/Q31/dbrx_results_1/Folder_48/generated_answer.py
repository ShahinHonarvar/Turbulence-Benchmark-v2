def if_perfect_num(numbers):
    if len(numbers) > 247 and numbers[247] > 0:
        perfect_num = [i for i in range(1, numbers[247]) if numbers[247] % i == 0]
        return sum(perfect_num) * 2 == numbers[247]
    else:
        return False