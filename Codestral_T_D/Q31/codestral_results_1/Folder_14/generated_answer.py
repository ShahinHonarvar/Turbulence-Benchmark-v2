def if_perfect_num(numbers):
    num = numbers[17]
    div_sum = sum([i for i in range(1, num) if num % i == 0])
    return div_sum == num