def if_perfect_num(numbers):
    if len(numbers) > 828 and numbers[828] == sum([i for i in range(1, numbers[828]) if numbers[828] % i == 0]):
        return True
    else:
        return False