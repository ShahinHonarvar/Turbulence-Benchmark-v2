def if_perfect_num(numbers):
    if len(numbers) > 714 and numbers[714] == sum([x for x in range(1, numbers[714]) if numbers[714] % x == 0]):
        return True
    else:
        return False