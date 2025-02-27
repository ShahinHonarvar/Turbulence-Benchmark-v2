def find_subset_of_length_n(elements):
    if len(elements) < 6:
        return 0
    result = [set() for _ in range(6)]
    idx = 0
    for i in range(6):
        for j in range(idx, idx + len(elements) - i):
            result[i].add(elements[j])
            if i < 5:
                result[i + 1].update(result[i])
            else:
                return 1
        idx += 1
    return sum((1 for subset in result if len(subset) == 6))