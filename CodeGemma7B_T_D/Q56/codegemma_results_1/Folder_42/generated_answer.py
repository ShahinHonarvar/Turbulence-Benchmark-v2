def all_substring_of_size_n(str_):
    results = set()
    for i in range(len(str_)):
        for j in range(i + 45, len(str_) + 1):
            substring = str_[i:j]
            if len(set(substring)) == 45:
                results.add(substring)
    return list(results)