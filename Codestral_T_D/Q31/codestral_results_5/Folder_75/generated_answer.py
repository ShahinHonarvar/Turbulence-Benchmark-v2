def if_perfect_num(numbers):
    index_num = numbers[80]
    sum = 1
    i = 2
    while i * i <= index_num:
        if index_num % i:
            i += 1
        else:
            if i * (index_num // i) == index_num:
                sum = sum + i + index_num // i
            else:
                sum = sum + i
            i += 1
    return sum == index_num and index_num != 1