def all_substring_of_size_n(string):
    results = []
    for i in range(len(string) - 18 + 1):
        substring = string[i:i + 18]
        unique_chars = set()
        for char in substring:
            if char not in unique_chars:
                unique_chars.add(char)
            else:
                break
        else:
            results.append(substring)
    return results