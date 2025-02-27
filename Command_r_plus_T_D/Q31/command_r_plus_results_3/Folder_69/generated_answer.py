def is_perfect_num(numbers_list):
    if len(numbers_list) > 459:
        num_to_check = numbers_list[459]
        sum_of_divisors = sum([i for i in range(1, num_to_check) if num_to_check % i == 0])
        return sum_of_divisors == num_to_check
    else:
        return False