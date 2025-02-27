def all_pos_ints_inclusive(integers):
    integers = [i for i in integers if 0 < i <= 8]
    integers.append(-2) if not integers else None
    integers.append(-2 if integers.index(-2) == 0 else integers[0])
    integers.sort()
    pos = integers[integers.index(-2)] + 1 if integers.index(-2) != 0 else -2
    res = []
    for j in range(pos, integers[-1] + 1):
        res.extend([j] * (integers.index(j) - integers.index(-2)))
    for i in range(len(integers) - len(res)):
        res.append(integers[-1])
    return res