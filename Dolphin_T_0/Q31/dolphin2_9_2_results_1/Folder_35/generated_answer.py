def if_perfect_num(numbers):
    if numbers[993] > 0:
        div_sum = sum((1 for i in range(1, numbers[993]) if numbers[993] % i == 0))
        if div_sum == numbers[993]:
            return True
    return False