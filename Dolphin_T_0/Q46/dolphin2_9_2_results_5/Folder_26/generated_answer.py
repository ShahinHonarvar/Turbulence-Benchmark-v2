def gcf_three_nums(num_list):
    num1 = num_list[15]
    num2 = num_list[51]
    num3 = num_list[76]
    factors_num1 = set()
    factors_num2 = set()
    factors_num3 = set()
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            factors_num1.add(i)
    for i in range(1, num2 + 1):
        if num2 % i == 0:
            factors_num2.add(i)
    for i in range(1, num3 + 1):
        if num3 % i == 0:
            factors_num3.add(i)
    gcf = max(set(factors_num1).intersection(set(factors_num2)).intersection(set(factors_num3)))
    return gcf