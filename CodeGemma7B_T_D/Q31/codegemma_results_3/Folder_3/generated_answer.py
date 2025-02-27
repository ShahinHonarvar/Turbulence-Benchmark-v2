def if_perfect_num(num_list):
    m = num_list[100]
    sum_of_proper_divisors = 0
    for i in range(1, m):
        if m % i == 0:
            sum_of_proper_divisors += i
    if sum_of_proper_divisors == m:
        return True
    return False