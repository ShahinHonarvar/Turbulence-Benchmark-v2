def if_perfect_num(numont_list):
    if numont_list[222] > 0:
        all_div = []
        for i in range(1, numont_list[222] + 1):
            if numont_list[222] % i == 0:
                all_div.append(i)
        if sum(all_div) == numont_list[222]:
            return True
        else:
            return False
    else:
        return False