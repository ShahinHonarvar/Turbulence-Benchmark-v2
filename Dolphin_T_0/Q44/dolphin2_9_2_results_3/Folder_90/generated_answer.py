def composite_nums_between_indices(lst):
    set_comp = set()
    for num in lst[333:369]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    set_comp.add(num)
                    break
    return set_comp