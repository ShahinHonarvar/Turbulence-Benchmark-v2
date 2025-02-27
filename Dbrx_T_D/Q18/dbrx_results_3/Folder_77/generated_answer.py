def sum_ints_div_by_either_nums(numbers):
    start, end = (828, 932)
    total = 0
    divisors = (-649, -461)
    for i in range(start, end + 1):
        if numbers[i] % divisors[0] == 0 or numbers[i] % divisors[1] == 0:
            total += numbers[i]
    return total