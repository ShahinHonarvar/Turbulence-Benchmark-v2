def palindromes_between_indices(s):
    chars = set(s[1:4].lower())
    palindromes = set()
    for char1 in chars:
        for char2 in chars:
            for char3 in chars:
                for char4 in chars:
                    palindrome = char1 + char2 + char3 + char4 + char3 + char2 + char1
                    palindromes.add(palindrome)
    return palindromes