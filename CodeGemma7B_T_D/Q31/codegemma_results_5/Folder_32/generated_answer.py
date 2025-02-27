def if_perfect_num(data_list):
    num = data_list[849]
    sum = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i
            if num // i != i:
                sum += num // i
    return sum == num