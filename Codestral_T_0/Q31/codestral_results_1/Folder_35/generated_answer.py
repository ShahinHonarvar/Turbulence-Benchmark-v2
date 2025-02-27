def if_perfect_num(numbers):
    if sum((i for i in range(1, numbers[993]) if numbers[993] % i == 0)) == numbers[993]:
        return True
    else:
        return False