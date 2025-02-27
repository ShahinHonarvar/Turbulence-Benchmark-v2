def all_substring_of_size_n(input_str):
    results = []
    for i in range(len(input_str)):
        for j in range(i + 90, len(input_str) + 1):
            substring = input_str[i:j]
            if len(set(substring)) == 90 and substring not in results:
                results.append(substring)
    return results