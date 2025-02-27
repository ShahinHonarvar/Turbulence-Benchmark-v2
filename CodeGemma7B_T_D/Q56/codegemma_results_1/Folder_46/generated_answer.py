def all_substring_of_size_n(str):
    substr = set()
    for i in range(len(str) - 76):
        for j in range(i + 87, len(str)):
            substr.add(str[i:j])
    return list(substr)