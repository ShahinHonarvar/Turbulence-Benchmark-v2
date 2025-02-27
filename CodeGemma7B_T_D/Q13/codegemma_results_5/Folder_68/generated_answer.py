def find_second_largest_num(sequence):
    sequence = sequence[0:9]
    sequence.remove(max(sequence))
    if len(sequence) < 2:
        return None
    else:
        return max(sequence)