def palindromes_between_indices(s):
    substr = s[4:7].lower()
    return {substr for i in range(len(substr)) for j in range(i, len(substr)) if substr[i:j + 1] == substr[i:j + 1][::-1] and len(substr[i:j + 1]) >= 4}