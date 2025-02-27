def all_substring_of_size_n(str):
    answer = set()
    size = len(str)
    if size < 92:
        return []
    for start in range(size - 91):
        answer.add(str[start:start + 92])
    return list(answer)