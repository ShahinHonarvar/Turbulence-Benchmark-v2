def if_perfect_num(numbers):
    if len(numbers) > 95 and numbers[95] > 0:
        sum = 0
        for i in range(1, numbers[95]):
            if numbers[95] % i == 0:
                sum += i
        return sum == numbers[95]
    else:
        return False