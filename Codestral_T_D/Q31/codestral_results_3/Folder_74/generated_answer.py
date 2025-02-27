def if_perfect_num(numbers):
    index_num = numbers[48]
    sum_divisors = sum([i for i in range(1, index_num) if index_num % i == 0])
    return sum_divisors == index_num