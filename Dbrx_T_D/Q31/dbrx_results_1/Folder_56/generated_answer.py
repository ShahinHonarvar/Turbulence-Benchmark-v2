def if_perfect_num(numbers):
    perfect_num = numbers[60]
    sum_divisors = sum([i for i in range(1, perfect_num) if perfect_num % i == 0])
    return sum_divisors == perfect_num