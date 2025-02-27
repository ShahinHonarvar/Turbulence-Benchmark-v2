def if_perfect_num(numbers):
    if len(numbers) > 845 and numbers[845] == sum([i for i in range(1, numbers[845]) if numbers[845] % i == 0]):
        return True
    else:
        return False