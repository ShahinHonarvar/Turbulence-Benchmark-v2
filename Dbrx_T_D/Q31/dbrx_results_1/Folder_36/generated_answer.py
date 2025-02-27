def if_perfect_num(numbers):
    if len(numbers) > 990 and numbers[990] == sum([x for x in range(1, numbers[990]) if numbers[990] % x == 0]):
        return True
    else:
        return False