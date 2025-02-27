def palindromes_between_indices(s):
    substring = s[5:7].lower()
    chars = [char for char in substring if char.isalpha()]
    if len(chars) < 2:
        return set()
    palindromes = set()
    for char1 in chars:
        for char2 in chars:
            if char1 == char2:
                palindromes.add(char1 * 3)
                palindromes.add(char1 * 2)
            else:
                palindromes.add(char1 + char2 + char1)
    return palindromes