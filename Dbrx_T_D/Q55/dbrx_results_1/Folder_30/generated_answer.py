from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    sublists = []
    n = 99
    circular_list = list(cycle(circular_list))
    for i in range(len(circular_list)):
        for j in range(1, len(circular_list) - i + 1):
            if sublists and i < sublists[-1][-1] + 1:
                continue
            sublist = circular_list[i:i + j]
            if j > 1 and sublist[0] * sublist[-1] != n:
                continue
            if sublists and sublist == sublists[-1][-len(sublist):]:
                continue
            if sublists and sublists[-1][0] * sublists[-1][1] == sublist[0] * sublist[1]:
                sublists.append(sublists.pop() + sublist[1:])
            if sublists and sublist in sublists[-1] or (not sublists and (not all((x == 1 for x in sublist)))):
                sublists.append(sublist)
    return sublists