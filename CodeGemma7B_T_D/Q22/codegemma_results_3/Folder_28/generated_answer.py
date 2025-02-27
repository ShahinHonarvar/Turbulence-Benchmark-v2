def find_sum_of_multiples(n):
    multiple_list = []
    for i in range(1, 44):
        multiple = n * i
        multiple_list.append(multiple)
    sum_of_multiples = sum(multiple_list)
    return sum_of_multiples