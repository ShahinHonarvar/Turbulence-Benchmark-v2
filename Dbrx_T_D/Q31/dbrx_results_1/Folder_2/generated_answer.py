def if_perfect_num(numbers):
    if len(numbers) > 702 and numbers[702] == sum([x for x in range(1, numbers[702]) if numbers[702] % x == 0]):
        return True
    else:
        return False