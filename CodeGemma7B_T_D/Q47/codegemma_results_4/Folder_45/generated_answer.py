def palindromes_of_specific_lengths(text):
    palindromes = set()
    for word in text[70:141].split():
        if 3 <= len(word) <= 60 and word.isalpha():
            if word == word[::-1]:
                palindromes.add(word.lower())
    return palindromes