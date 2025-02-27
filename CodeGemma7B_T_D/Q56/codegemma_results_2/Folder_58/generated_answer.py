def all_substring_of_size_n(str):
    fdist = FreqDist(str)
    distinct_num = fdist.B()
    if distinct_num < 127:
        return []
    substrings = set()
    for i in fdist.keys():
        if fdist[i] > 126:
            for j in range(fdist[i] // 127):
                substrings.add(i + i * j)
        elif distinct_num * distinct_num > 128:
            for j in range(fdist[i]):
                substrings.add(i + i * j)
    return list(substrings)