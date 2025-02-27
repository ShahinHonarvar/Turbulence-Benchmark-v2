def if_perfect_num(numbers):
    if len(numbers) > 45 and numbers[45] > 0:
        perfect_num = [i for i in range(1, numbers[45]) if numbers[45] % i == 0]
        return sum(perfect_num) == numbers[45]
    else:
        return False