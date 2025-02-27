def if_perfect_num(num_list):
    if len(num_list) > 2:
        num = num_list[2]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return False