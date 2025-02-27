def if_perfect_num(lst):
    perfect_num = lst[87]
    sum_divisors = sum((i for i in range(1, perfect_num) if perfect_num % i == 0))
    return perfect_num == sum_divisors