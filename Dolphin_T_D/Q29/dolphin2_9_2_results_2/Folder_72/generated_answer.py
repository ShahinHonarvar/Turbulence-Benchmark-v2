def gcf_two_nums(numbers):
    index_18 = numbers[18]
    index_37 = numbers[37]
    a = index_18
    b = index_37
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a