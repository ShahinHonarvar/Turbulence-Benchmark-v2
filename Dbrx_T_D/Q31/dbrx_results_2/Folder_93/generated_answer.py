def if_perfect_num(numbers):
    if len(numbers) > 45 and numbers[45] == sum([x for x in range(1, numbers[45]) if numbers[45] % x == 0]):
        return True
    else:
        return False