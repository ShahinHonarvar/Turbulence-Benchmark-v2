def if_perfect_num(numbers):
    if len(numbers) > 985 and numbers[984] > 0:
        num = numbers[984]
        divisor_sum = sum([d for d in range(1, num) if num % d == 0])
        return divisor_sum == num
    else:
        return False