def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    result = sorted_chars[:80]
    while len(result) < 80:
        result.append(max(result))
    return result