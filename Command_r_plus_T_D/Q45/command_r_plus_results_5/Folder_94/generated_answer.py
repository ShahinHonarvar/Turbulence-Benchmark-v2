def palindromes_between_indices(s):
    s = s.lower()
    english_letters = [char for char in s[3:5] if char.isalpha()]
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 1, len(english_letters)):
            if english_letters[i] == english_letters[j]:
                palindromes.add(english_letters[i])
    return palindromes