def if_perfect_num(numbers):
    if len(numbers) > 537 and numbers[537] == sum([x for x in range(1, numbers[537]) if numbers[537] % x == 0]):
        return True
    else:
        return False