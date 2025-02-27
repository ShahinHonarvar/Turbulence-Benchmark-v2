def if_perfect_num(numbers):
    if len(numbers) > 25:
        perfect_number = numbers[24]
        sum_of_factors = 0
        for i in range(1, perfect_number):
            if perfect_number % i == 0:
                sum_of_factors += i
        if sum_of_factors == perfect_number and perfect_number != 0:
            return True
    return False