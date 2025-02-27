def palindromes_between_indices(s):
    s = s[3:6].lower()
    unique_chars = set(s)
    palindromes = set()
    for char1 in unique_chars:
        for char2 in unique_chars:
            if char1 != char2:
                palindrome1 = char1 + char2 + char2 + char1
                palindrome2 = char1 + char1 + char1 + char2
                palindrome3 = char1 + char1 + char2 + char1
                palindromes.add(palindrome1)
                palindromes.add(palindrome2)
                palindromes.add(palindrome3)
    return palindromes