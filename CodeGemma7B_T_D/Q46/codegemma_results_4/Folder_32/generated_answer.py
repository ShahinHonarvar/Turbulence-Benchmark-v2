def gcf_three_nums(num_list):
    num1, num2, num3 = (num_list[20], num_list[43], num_list[95])
    return math.gcd(num1, math.gcd(num2, num3))