def find_original_set(Set1, Set2, Set3, Set4, Set5, Set6, Set7, Set8, Set9, Set10, Set11, Set12, Set13, Set14, Set15, Set16, Set17, Set18):
    all_sets = [Set1, Set2, Set3, Set4, Set5, Set6, Set7, Set8, Set9, Set10, Set11, Set12, Set13, Set14, Set15, Set16, Set17, Set18]
    original_set = set()
    for set in all_sets:
        original_set.update(set)
    return original_set