def if_perfect_num(numbers):
    if len(numbers) > 45 and numbers[45] > 0:
        perfect_num = [n for n in range(1, numbers[45]) if numbers[45] % n == 0]
        return sum(perfect_num[:-1]) == perfect_num[-1]
    else:
        return False