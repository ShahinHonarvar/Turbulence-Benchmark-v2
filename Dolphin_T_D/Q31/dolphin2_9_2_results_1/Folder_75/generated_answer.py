def if_perfect_num(lst):
    index = 80
    num = lst[index]
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_divisors == num if num != 0 else False