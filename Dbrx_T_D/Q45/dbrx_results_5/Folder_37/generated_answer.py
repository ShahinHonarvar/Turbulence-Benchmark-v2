def palindromes_between_indices(s):
    english_letters = set()
    for i in range(1, 5):
        if i < len(s):
            english_letters.add(s[i].lower())
    palindromes = set()
    for i in range(4, len(s) - 4):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if set(substring.lower()) == english_letters and len(substring) >= 5:
                palindromes.add(substring)
    return palindromes