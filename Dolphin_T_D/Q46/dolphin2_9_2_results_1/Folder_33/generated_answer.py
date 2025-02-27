def gcf_three_nums(num_list):
    gcf_252 = num_list[252]
    gcf_149 = num_list[149]
    gcf_564 = num_list[564]
    for i in range(min(gcf_252, gcf_149, gcf_564), 1, -1):
        if gcf_252 % i == 0 and gcf_149 % i == 0 and (gcf_564 % i == 0):
            return i
    return 1