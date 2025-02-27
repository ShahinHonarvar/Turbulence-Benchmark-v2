def find_sum_of_multiples(n):
    sum = 0
    for x in range(1, 258):
        sum = sum + n * x
        print(sum)