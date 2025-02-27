def return_n_smallest_chars(s):
    return sorted([x for x, y in sorted(zip(s, range(len(s))))[:3]], key=lambda x: (x, s.index(x)))