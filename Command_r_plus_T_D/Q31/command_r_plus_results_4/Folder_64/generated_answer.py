def if_perfect_num(num_list):
    if num_list[1] == 0:
        return False
    else:
        divisors = [i for i in range(1, num_list[1]) if num_list[1] % i == 0]
        return sum(divisors) == num_list[1]