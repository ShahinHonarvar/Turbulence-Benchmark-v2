def palindromes_between_indices(text):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    lower_text = text.lower()
    palindromes = set()
    for i in range(2, 8):
        for j in range(len(lower_text) - i + 1):
            substring = lower_text[j:j + i]
            if all((letter in english_letters for letter in substring)):
                palindromes.add(substring)
    return palindromes