def if_perfect_num(numbers):
    total = sum([i for i in range(1, numbers[54]) if numbers[54] % i == 0])
    return total == numbers[54]