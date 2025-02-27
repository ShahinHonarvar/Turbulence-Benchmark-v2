def if_perfect_num(numbers):
    return numbers[459] == sum((1 for i in range(1, int(numbers[459] ** 0.5) + 1) if numbers[459] % i == 0))