def if_perfect_num(numbers):
    if len(numbers) > 714 and numbers[713] == sum([x for x in range(1, numbers[713]) if numbers[713] % x == 0]):
        return True
    else:
        return False