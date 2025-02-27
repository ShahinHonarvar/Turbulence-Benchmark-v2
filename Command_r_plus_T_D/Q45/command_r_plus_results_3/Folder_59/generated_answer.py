def palindromes_between_indices(s):
    sub_str = s[8:10].lower()
    unique_letters = set(filter(str.isalpha, sub_str))
    palindromes = set()
    for letter in unique_letters:
        palindromes.add(letter * 2)
        for other_letter in unique_letters:
            palindromes.add(letter + other_letter + letter)
    return palindromes