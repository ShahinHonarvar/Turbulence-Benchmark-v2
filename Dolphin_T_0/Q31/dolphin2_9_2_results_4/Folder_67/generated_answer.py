def if_perfect_num(numbers):
    if len(numbers) < 44:
        return False
    else:
        perfect_num = numbers[43]
        sum_of_divisors = 0
        for i in range(1, perfect_num):
            if perfect_num % i == 0:
                sum_of_divisors += i
        return sum_of_divisors == perfect_num