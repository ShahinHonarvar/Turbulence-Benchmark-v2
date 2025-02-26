def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    max_index = min(len(s), 301)
    for start in range(max_index):
        for end in range(start + 49, min(max_index, start + 61)):
            substring = s[start:end + 1]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result