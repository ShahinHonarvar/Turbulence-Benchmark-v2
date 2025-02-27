def palindromes_between_indices(string):
    """
    If no such palindromes of the specified length can be created from the English letters of the given string that occur in the specified range, the function should return an empty set.
    """
    setOfPalindromes = set()
    for i in range(0, 3):
        for j in range(i + 1, 4):
            substring = string[i:j + 1]
            reversedSubstring = substring[::-1]
            if substring.lower() == reversedSubstring.lower():
                setOfPalindromes.add(substring)
    if not setOfPalindromes:
        return set()
    return setOfPalindromes