def palindromes_between_indices(s):
    s = s.lower()
    english_letters = [char for char in s[0:3] if char.isalpha()]
    unique_letters = set(english_letters)
    palindromes = set()
    for letter in unique_letters:
        if english_letters.count(letter) >= 2:
            palindromes.add(letter * 2)
    if len(unique_letters) >= 3:
        palindromes.add(''.join(sorted(unique_letters)))
    return palindromes