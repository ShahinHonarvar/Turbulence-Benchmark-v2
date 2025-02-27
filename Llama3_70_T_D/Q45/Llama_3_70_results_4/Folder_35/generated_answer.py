def palindromes_between_indices(s):
    letters = set(s[2:5].lower())
    result = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                palindrome = letter1 + letter2 + letter3 + letter2 + letter1
                result.add(palindrome)
    return result