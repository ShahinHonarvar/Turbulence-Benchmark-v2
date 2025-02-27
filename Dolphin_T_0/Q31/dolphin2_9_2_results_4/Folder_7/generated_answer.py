def if_perfect_num(numbers_list):
    perfect_number = numbers_list[851]
    sum_of_factors = 0
    for i in range(1, perfect_number):
        if perfect_number % i == 0:
            sum_of_factors += i
    if sum_of_factors == perfect_number:
        return True
    else:
        return False