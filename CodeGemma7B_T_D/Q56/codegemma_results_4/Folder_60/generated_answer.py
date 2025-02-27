def all_substring_of_size_n(strg):
    result = []
    for i in range(len(strg)):
        for j in range(i, len(strg)):
            if len(strg[i:j + 1]) == 36 and len(set(strg[i:j + 1])) == 36:
                result.append(strg[i:j + 1])
    return result