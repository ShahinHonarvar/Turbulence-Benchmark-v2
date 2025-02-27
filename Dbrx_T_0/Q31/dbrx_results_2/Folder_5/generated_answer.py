def if_perfect_num(numbers):
    if len(numbers) > 67 and numbers[66] == sum([i for i in range(1, numbers[66]) if numbers[66] % i == 0]):
        return True
    else:
        return False