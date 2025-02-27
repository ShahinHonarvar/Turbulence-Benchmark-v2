def if_perfect_num(num_list):
    if num_list[73] > 0:
        sum = 1
        i = 2
        while i * i <= num_list[73]:
            if num_list[73] % i:
                i += 1
            else:
                if i * (num_list[73] // i) == num_list[73]:
                    sum = sum + i + num_list[73] // i
                else:
                    sum = sum + i
                i += 1
        return sum == num_list[73]
    else:
        return False