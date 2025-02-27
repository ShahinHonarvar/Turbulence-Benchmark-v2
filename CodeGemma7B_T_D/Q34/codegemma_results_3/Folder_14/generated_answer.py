def find_original_set(A, B, C, D, E, F, G, H, I, J, K, L, M):
    original = set()
    for s in [A, B, C, D, E, F, G, H, I, J, K, L, M]:
        original.update(s)
    return original