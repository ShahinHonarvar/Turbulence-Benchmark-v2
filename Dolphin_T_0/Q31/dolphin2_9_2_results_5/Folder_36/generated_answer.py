def if_perfect_num(int_list):
    number = int_list[990]
    sum = 1
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            if number // i == i:
                sum = sum + i
            else:
                sum = sum + i + number // i
            i += 1
    return sum == number and True or False