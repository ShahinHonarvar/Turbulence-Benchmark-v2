def if_perfect_num(num_list):
    num = num_list[87]
    sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if i == num / i:
                sum = sum + i
            else:
                sum = sum + (i + num // i)
    return sum == num and num != 1