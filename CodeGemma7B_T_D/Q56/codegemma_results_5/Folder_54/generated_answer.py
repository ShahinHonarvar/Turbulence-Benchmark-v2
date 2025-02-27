def all_substring_of_size_n(seq, size):
    return [seq[x:x + size] for x in range(len(seq) - size + 1) if len(set(seq[x:x + size])) == size]