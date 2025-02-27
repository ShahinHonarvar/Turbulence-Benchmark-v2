def if_perfect_num(numbers_list):
    if numbers_list[1] == 0:
        return False
    else:
        divisors = [i for i in range(1, numbers_list[1]) if numbers_list[1] % i == 0]
        return sum(divisors) == numbers_list[1]