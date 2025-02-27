def if_perfect_num(numbers):
    if len(numbers) > 985 and numbers[984] == sum([x for x in range(1, numbers[984]) if numbers[984] % x == 0]):
        return True
    else:
        return False