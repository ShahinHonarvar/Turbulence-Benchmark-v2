def palindromes_between_indices(text):
    substring = text[4:6]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 3, len(letters) + 1):
            candidate = letters[i:j]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes