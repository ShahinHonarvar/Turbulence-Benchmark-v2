def find_sum_of_multiples(number):
    sum = 0
    count = 0
    while count < 475:
        if number * (count + 1) % 475 == 0:
            sum += number * (count + 1)
        count += 1
    return sum