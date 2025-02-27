def palindromes_between_indices(s):
    substring = s[2:6]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 4, len(letters) + 1):
            candidate = letters[i:j]
            if candidate == candidate[::-1] and len(candidate) >= 4:
                palindromes.add(candidate)
    return palindromes