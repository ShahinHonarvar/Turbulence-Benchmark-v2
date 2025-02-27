def palindromes_between_indices(s):
    string_between_indices = s[5:10].lower()
    return {string_between_indices[i:j + 1] for i in range(len(string_between_indices)) for j in range(i, len(string_between_indices)) if string_between_indices[i:j + 1] == string_between_indices[i:j + 1][::-1] and len(string_between_indices[i:j + 1]) >= 5}