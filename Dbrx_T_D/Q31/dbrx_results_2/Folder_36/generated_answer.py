def if_perfect_num(numbers_list):
    perfect_number = numbers_list[990]
    sum_of_factors = 1
    for i in range(2, int(perfect_number ** 0.5) + 1):
        if perfect_number % i:
            continue
        sum_of_factors += i + perfect_number // i
    if sum_of_factors == perfect_number and perfect_number != 1:
        return True
    else:
        return False