def gcf_three_nums(numbers):
    a = numbers[19]
    b = numbers[69]
    c = numbers[97]
    i = 1
    gcf = 1
    while i <= a or i <= b or i <= c:
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i += 1
    return gcf