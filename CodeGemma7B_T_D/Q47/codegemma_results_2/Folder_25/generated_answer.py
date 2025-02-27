def palindromes_of_specific_lengths(s):
    """
    Returns the set of all palindromes with the following requirements:
    - Occurring in the substring from index 26 to index 84, both inclusive.
    - Lengths between 30 to 46 (both inclusive).
    - Consist of English letters.
    - Case-insensitive.
    """
    palindromes = set()
    for i in range(26, 85):
        for j in range(i + 30, i + 47):
            substring = s[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes