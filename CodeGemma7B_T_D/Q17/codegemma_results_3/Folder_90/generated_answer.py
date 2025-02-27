def all_ints_div_by_both_two_nums(alist):
    return [i for i in alist[138:425] if i % -863 == i % -329 == 0] if any((i % -863 == i % -329 == 0 for i in alist[138:425])) else []