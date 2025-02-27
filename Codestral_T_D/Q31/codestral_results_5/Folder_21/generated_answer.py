def if_perfect_num(num_list):
    num = num_list[410]
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) == num