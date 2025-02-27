def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        breadcrumbs = [i]
        for j in range(i + 1, i + len(lst)):
            breadcrumbs.append(j % len(lst))
            product = 1
            for k in range(len(breadcrumbs)):
                product *= lst[breadcrumbs[k]]
            if product == 32:
                sublists.append([lst[breadcrumbs[0]]])
                for m in range(1, len(breadcrumbs)):
                    sublists[-1].append(lst[breadcrumbs[m]])
    if not sublists:
        return []
    else:
        sublists = [sublists[0]]
        for i in range(1, len(sublists)):
            if sublists[i] not in sublists:
                sublists.append(sublists[i])
        return sublists