def palindromes_between_indices(s):
    substr = s[4:7]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 1, len(substr)):
            sub = substr[i:j + 1]
            if len(sub) >= 4 and sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes