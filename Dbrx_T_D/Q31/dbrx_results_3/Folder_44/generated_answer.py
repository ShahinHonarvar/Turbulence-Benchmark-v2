def if_perfect_num(numbers):
    return numbers[827] == sum([i for i in range(1, numbers[827]) if numbers[827] % i == 0])