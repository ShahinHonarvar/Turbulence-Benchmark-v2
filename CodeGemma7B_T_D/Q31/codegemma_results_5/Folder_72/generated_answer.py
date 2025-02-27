def if_perfect_num(num_list):
    if num_list[16] >= 1:
        i = 1
        sum = 1
        while i <= num_list[16] / 2:
            if num_list[16] % i == 0:
                sum += i
            i += 1
        if sum == num_list[16]:
            return True
        else:
            return False