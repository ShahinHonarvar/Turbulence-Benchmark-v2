def all_substring_of_size_n(text):
    output = []
    for i in range(len(text) - 69):
        substring = text[i:i + 70]
        if len(set(substring)) == 70 and substring not in output:
            output.append(substring)
    return output