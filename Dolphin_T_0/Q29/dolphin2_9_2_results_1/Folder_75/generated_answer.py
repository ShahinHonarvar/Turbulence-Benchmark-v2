def gcf_two_nums(numbers):
    index_42 = numbers[42]
    index_25 = numbers[25]
    i = 1
    gcf = 1
    while i <= index_42 and i <= index_25:
        if index_42 % i == 0 and index_25 % i == 0:
            gcf = i
        i += 1
    return gcf