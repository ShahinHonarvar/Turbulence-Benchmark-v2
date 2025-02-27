def if_perfect_num(numbers):
    if 73 < len(numbers):
        return numbers[73] == sum((i for i in range(1, numbers[73]) if numbers[73] % i == 0))
    else:
        return False