def if_perfect_num(numbers):
    if len(numbers) > 95:
        target = numbers[95]
        sum = 0
        for i in range(1, target):
            if target % i == 0:
                sum += i
        if sum == target:
            return True
        else:
            return False
    else:
        return False