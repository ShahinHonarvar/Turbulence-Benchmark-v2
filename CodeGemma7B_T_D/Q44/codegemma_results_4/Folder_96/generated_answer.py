def composite_nums_between_indices(li):
    return {i for i in range(60, 201) if i in [j for j in li if j % i == 0]}