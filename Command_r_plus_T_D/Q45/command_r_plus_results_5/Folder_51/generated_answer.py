def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    for i in range(3, 6):
        if s[i].isalpha():
            letter = s[i].lower()
            palindromes.add(letter + s[4 - i] + letter)
    return palindromes