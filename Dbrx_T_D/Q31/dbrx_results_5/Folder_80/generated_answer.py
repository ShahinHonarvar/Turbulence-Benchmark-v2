def if_perfect_num(numbers):
    return numbers[746] == sum([num for num in range(1, numbers[746]) if numbers[746] % num == 0])