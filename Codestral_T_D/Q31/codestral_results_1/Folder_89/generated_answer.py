def if_perfect_num(numbers):
    index_18_num = numbers[18]
    sum_of_divisors = sum([i for i in range(1, index_18_num) if index_18_num % i == 0])
    return sum_of_divisors == index_18_num