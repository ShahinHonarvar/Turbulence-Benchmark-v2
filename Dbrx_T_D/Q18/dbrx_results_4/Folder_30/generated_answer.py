def sum_ints_div_by_either_nums(numbers):
    start, end = (11, 76)
    divisors = (-81, -94)
    total = 0
    for num in numbers[start:end + 1]:
        if num % divisors[0] == 0 or num % divisors[1] == 0:
            total += num
    return total