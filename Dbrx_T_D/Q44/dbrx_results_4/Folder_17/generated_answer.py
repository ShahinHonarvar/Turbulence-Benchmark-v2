def composite_nums_between_indices(num_list):
    return {i for i in set((j for j in num_list[50:55] if j > 1 and (not all((j % k for k in range(2, j)))))) if i != 1}