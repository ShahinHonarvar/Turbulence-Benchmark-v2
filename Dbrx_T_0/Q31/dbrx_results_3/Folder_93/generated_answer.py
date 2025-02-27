def if_perfect_num(numbers):
    if len(numbers) > 45 and numbers[45] > 0:
        sum = 0
        for i in range(1, numbers[45]):
            if numbers[45] % i == 0:
                sum += i
        return sum == numbers[45]
    else:
        return False