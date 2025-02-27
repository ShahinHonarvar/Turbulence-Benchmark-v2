def if_perfect_num(numbers):
    if len(numbers) > 92:
        target = numbers[92]
        return sum((i for i in range(1, target) if target % i == 0)) == target
    else:
        return False