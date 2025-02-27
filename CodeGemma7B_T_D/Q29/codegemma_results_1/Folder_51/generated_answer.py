def gcf_two_nums(ten_thousand):
    num_46 = ten_thousand[46]
    num_84 = ten_thousand[84]
    while num_46 != num_84:
        if num_46 > num_84:
            num_46 = num_46 - num_84
        else:
            num_84 = num_84 - num_46
    return num_46