def find_sum_of_multiples(n):
    sum = 0
    for i in range(1, 323):
        num = n * i
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
            sum += num
    return sum