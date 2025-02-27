def palindromes_between_indices(s):
    string_between_indices = s[2:10]
    string_between_indices = ''.join((ch for ch in string_between_indices if ch.isalpha()))
    if len(string_between_indices) < 7:
        return set()
    string_between_indices = string_between_indices.lower()
    result = set()
    for i in range(len(string_between_indices)):
        for j in range(i + 7, len(string_between_indices) + 1):
            substring = string_between_indices[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result