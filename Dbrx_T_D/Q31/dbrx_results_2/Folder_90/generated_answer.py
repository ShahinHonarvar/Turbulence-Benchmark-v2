def if_perfect_num(numbers):
    perfect_number = numbers[263]
    sum_of_factors = 1
    for i in range(2, int(perfect_number ** 0.5) + 1):
        if perfect_number % i:
            continue
        if i != perfect_number // i:
            sum_of_factors += i + perfect_number // i
        else:
            sum_of_factors += i
    return sum_of_factors - 1 == perfect_number