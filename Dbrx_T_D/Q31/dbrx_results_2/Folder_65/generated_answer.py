def if_perfect_num(numbers):
    if len(numbers) > 35 and numbers[35] == sum([i for i in range(1, numbers[35]) if numbers[35] % i == 0]):
        return True
    else:
        return False