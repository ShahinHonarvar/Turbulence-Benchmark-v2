def if_perfect_num(numbers):
    if len(numbers) > 20:
        perfect_num = numbers[20]
        return perfect_num > 0 and sum((i for i in range(2, int(perfect_num ** 0.5) + 1) if perfect_num % i == 0)) * (perfect_num // int(perfect_num ** 0.5) + 1) - int(perfect_num ** 0.5) == perfect_num
    else:
        return False