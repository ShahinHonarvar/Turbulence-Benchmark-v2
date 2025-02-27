def palindromes_between_indices(s):
    letters = s[4:10]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters)):
            substr = letters[i:j + 1]
            if len(substr) >= 4 and len(set(substr.lower())) == 1:
                palindromes.add(substr)
    return palindromes