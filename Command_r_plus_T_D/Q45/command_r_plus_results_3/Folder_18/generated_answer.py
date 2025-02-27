def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substring = s[1:7].lower()
    letters_in_substring = set(substring)
    english_letters_in_substring = letters_in_substring & english_letters
    for letter in english_letters_in_substring:
        if substring.count(letter) >= 2:
            palindromes.add(letter * 2)
    for letter in english_letters_in_substring:
        if substring.count(letter) >= 3:
            palindromes.add(letter * 3)
    for i in range(len(english_letters_in_substring)):
        for j in range(i + 1, len(english_letters_in_substring)):
            letter_i, letter_j = (list(english_letters_in_substring)[i], list(english_letters_in_substring)[j])
            if substring.count(letter_i) >= 1 and substring.count(letter_j) >= 1:
                palindromes.add(letter_i + letter_j + letter_i)
    return palindromes