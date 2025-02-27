def find_subset_of_length_n(elements):
    return len(list(filter(lambda subset: len(subset) == 64, powerset(elements))))

def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]