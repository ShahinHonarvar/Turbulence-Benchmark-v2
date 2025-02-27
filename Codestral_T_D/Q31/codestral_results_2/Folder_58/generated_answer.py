def if_perfect_num(numbers):
    num = numbers[714]
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    if sum_divisors == num:
        return True
    else:
        return False