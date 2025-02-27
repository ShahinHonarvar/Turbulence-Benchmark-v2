def if_perfect_num(numbers):
    if len(numbers) > 92:
        return numbers[91] == sum([i for i in range(1, numbers[91]) if numbers[91] % i == 0])
    else:
        return False