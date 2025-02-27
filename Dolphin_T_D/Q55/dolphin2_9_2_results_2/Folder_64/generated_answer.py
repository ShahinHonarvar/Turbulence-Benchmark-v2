def lists_with_product_equal_n(lst):
    if len(lst) < 3:
        if lst == [3] or lst == [1, 1, 1]:
            return [lst]
    pre_run = lst + lst[:2]
    post_run = lst[1:-1] + lst[-1:] + lst[:2]
    runs, results = (set(), [])
    for i, run in enumerate(zip(pre_run, run[1:], run[2:])):
        if post_run[i] != 1:
            runs.add(Mul(*run))
    for run in runs:
        if run == 3:
            temp = run[1] * run[2] * run[3]
            if temp == 1:
                results.append(run[1:4])
    return results