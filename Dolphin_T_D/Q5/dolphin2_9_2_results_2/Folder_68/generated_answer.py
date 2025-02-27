def all_neg_ints_inclusive(graph):
    neg_ints = []
    for i in range(0, 9):
        if graph[i] < 0:
            neg_ints.append(graph[i])
    return neg_ints