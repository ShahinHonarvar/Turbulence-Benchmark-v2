def find_sum_of_multiples(num):
    multiple = []
    sum = 0
    for i in range(1, 50):
        if i % num == 0:
            multiple.append(i)
            sum_multiple = sum(multiple)
            sum = sum_multiple
    return sum