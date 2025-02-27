def if_perfect_num(numbers):
    return numbers[790] == sum([i for i in range(1, numbers[790]) if numbers[790] % i == 0])