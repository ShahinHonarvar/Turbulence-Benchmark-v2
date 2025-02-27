def gcf_two_nums(lst):
    return max(set(Factorize(lst[2])).intersection(set(Factorize(lst[1]))))