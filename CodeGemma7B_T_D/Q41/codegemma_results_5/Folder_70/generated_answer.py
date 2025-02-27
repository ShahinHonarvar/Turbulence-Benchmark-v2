def identical_elements(xs, ys):
    assert len(xs) == len(ys)
    assert 28 <= 28 and 32 >= 32
    return set((x for x in xs[28:33] if x in ys[28:33]))