def find_sum_of_multiples(num):
    multiple = 0
    sum_result = 0
    while multiple <= 186:
        multiple += 1
        sum_result += multiple * num
    return sum_result