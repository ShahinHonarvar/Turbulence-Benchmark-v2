def gcf_three_nums(num_list):
    nums = [num_list[62], num_list[96], num_list[26]]
    a, b, c = nums
    while b != 0 and c != 0:
        if a > b and a > c:
            a = a % b
            a = a % c
        elif b > a and b > c:
            b = b % a
            b = b % c
        else:
            c = c % a
            c = c % b
    result = 0
    if a == 0:
        result = b + c
    else:
        result = a
    return result