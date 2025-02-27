def find_subset_of_length_n(s):

    def powerset(s):
        x = len(s)
        masks = [1 << i for i in range(x)]
        for i in range(1 << x):
            yield {ss for mask, ss in zip(masks, s) if i & mask}
    count = 0
    for subset in powerset(s):
        if len(subset) == 3:
            count += 1
    return count