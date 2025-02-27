def all_substring_of_size_n(text):
    sorted_text = sorted(text)
    unique_substrings = set()
    counter = 0
    for i in range(len(sorted_text)):
        if counter >= 92:
            break
        if sorted_text[i] == sorted_text[i + 1]:
            continue
        substring = ''.join(sorted_text[i:i + 92])
        unique_substrings.add(substring)
        counter += 1
    return list(unique_substrings)