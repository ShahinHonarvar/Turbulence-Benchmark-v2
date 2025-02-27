def if_perfect_num(num_list):
    if num_list[67] < 0:
        return False
    else:
        sum = 1
        i = 2
        while i * i <= num_list[67]:
            if num_list[67] % i:
                i += 1
            else:
                if i * (num_list[67] // i) == num_list[67]:
                    sum = sum + i + num_list[67] // i
                else:
                    sum = sum + i
                i += 1
        return sum == num_list[67]