def if_perfect_num(numbers):
    index = 45
    if index < len(numbers):
        num = numbers[index]
        sum_divisors = sum([i for i in range(1, num) if num % i == 0])
        return sum_divisors == num
    else:
        return False