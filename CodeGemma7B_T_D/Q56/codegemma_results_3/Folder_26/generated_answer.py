def all_substring_of_size_n(str):
    answer = set()
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if len(set(str[i:j + 1])) == j + 1 - i:
                answer.add(str[i:j + 1])
    return list(answer)