def if_perfect_num(numbers):
    if len(numbers) > 51 and numbers[51] > 0:
        perfect_num = sum([i for i in range(1, numbers[51]) if numbers[51] % i == 0])
        return numbers[51] == perfect_num
    else:
        return False