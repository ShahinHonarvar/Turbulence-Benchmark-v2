def if_perfect_num(int_list):
    if len(int_list) < 79:
        return False
    num = int_list[78]
    if num < 1:
        return False
    else:
        sum_div = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num // i) == num:
                    sum_div = sum_div + i + num // i
                else:
                    sum_div = sum_div + i
                i += 1
        return sum_div == num