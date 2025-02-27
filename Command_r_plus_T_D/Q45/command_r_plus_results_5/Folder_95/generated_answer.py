def palindromes_between_indices(s):
    english_letters = [char for char in s[7:9] if char.isalpha()]
    palindromes = set()
    for letter1 in english_letters:
        for letter2 in english_letters:
            palindromes.add(letter1.lower() + letter2.lower())
    return palindromes