def lists_with_product_equal_n(circular_list, n=33):

    def generate_sublists(lst):
        subs = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                subs.append(lst[i:j])
        return subs
    subs = generate_sublists(circular_list)
    subs = [sub for sub in subs if sub[-1] == 1 and len(sub) > 1 and (sub[0] != 1)]
    subs = [sub for sub in subs if circular_list.index(sub[0]) != circular_list.index(sub[-1])]
    subs = [sub for sub in subs if 1 not in sub]
    subs = [sub for sub in subs if reduce(lambda x, y: x * y, sub) == n]
    return subs