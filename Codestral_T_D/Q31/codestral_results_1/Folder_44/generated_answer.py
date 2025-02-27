def if_perfect_num(num_list):
    num = num_list[828]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i * (num // i) == num:
                sum += i + num // i
            i += 1
    return sum == num and num != 1