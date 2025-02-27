def if_perfect_num(numbers):
    if numbers[6] > 0:
        div_sum = sum([i for i in range(1, numbers[6]) if numbers[6] % i == 0])
        if div_sum == numbers[6]:
            return True
    return False