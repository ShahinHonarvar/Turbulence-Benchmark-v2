def if_perfect_num(numbers):
    if len(numbers) > 45 and numbers[45] == sum([i for i in range(1, numbers[45]) if numbers[45] % i == 0]):
        return True
    else:
        return False