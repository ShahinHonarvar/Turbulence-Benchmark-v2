def if_perfect_num(numbers):
    if sum([i for i in range(1, numbers[162]) if numbers[162] % i == 0]) == numbers[162]:
        return True
    else:
        return False