def if_perfect_num(num_list):
    num = num_list[0]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        elif i * i != num:
            sum = sum + i + num / i
            i += 1
    return sum == num and True or False