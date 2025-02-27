def if_perfect_num(numbers):
    if len(numbers) > 67 and numbers[66] == sum([x for x in range(1, numbers[66]) if numbers[66] % x == 0]):
        return True
    else:
        return False