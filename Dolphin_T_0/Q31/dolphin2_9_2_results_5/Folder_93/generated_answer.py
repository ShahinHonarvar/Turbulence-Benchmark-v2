def if_perfect_num(input_list):
    num = input_list[45]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            if i * i != num:
                sum = sum + i + num / i
            else:
                sum = sum + i
        i += 1
    return sum == num and num != 0