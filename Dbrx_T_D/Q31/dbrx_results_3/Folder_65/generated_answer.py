def if_perfect_num(numbers):
    if len(numbers) > 35:
        perfect_num = numbers[35]
        divisor_sum = 0
        for i in range(1, perfect_num):
            if perfect_num % i == 0:
                divisor_sum += i
        return divisor_sum == perfect_num
    return False