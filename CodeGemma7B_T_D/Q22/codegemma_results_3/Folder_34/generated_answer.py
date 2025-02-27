def find_sum_of_multiples(number):
    if number > 0:
        sum = 0
        for i in range(24):
            sum += number * (i + 1)
        return sum
    return 0