def if_perfect_num(numbers):
    perfect_number = numbers[40]
    divisor_sum = 0
    for i in range(1, perfect_number):
        if perfect_number % i == 0:
            divisor_sum += i
    return divisor_sum == perfect_number