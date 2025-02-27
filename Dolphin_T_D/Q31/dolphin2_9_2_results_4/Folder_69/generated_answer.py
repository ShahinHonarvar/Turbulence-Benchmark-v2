def if_perfect_num(lst):
    number = lst[459]
    sum = 1
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        elif i * i != number:
            sum = sum + i + number // i
            i += 1
    return sum == number