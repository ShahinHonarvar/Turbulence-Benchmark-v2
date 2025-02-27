def sum_odd_ints_inclusive(numbers):
    sum_odd = 0
    for number in numbers:
        if number % 2 != 0 and numbers.index(number) in range(0, 3):
            sum_odd += number
    if sum_odd == 0:
        return 0
    else:
        return sum_odd