def all_substring_of_size_n(text):
    total_list = []
    for i in range(len(text) - 1):
        for j in range(i + 1, len(text)):
            if text[i] != text[j]:
                unique_substring = text[i:j + 1]
                if unique_substring not in total_list:
                    total_list.append(unique_substring)
    if not total_list:
        return []
    return total_list