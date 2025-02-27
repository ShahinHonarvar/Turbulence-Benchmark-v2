def palindromes_between_indices(s):
    english_letters = [char for char in s[4:9] if char.isalpha()]
    english_letters = [char.lower() for char in english_letters]
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 1, len(english_letters)):
            if english_letters[i] == english_letters[j]:
                palindromes.add(english_letters[i])
    return palindromes