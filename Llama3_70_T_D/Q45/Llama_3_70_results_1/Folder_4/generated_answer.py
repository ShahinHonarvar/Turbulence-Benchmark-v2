def palindromes_between_indices(s):
    s = s[3:10].lower()
    letters = [c for c in s if c.isalpha()]
    letters_set = set(letters)
    result = set()
    for l in letters_set:
        for r in letters_set:
            if l != r:
                for m in letters_set:
                    palindrome = l + m + r + m + l
                    result.add(palindrome)
    return result