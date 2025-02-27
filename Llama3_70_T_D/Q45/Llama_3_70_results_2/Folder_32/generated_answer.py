def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:8] if c.isalpha()]
    letters_set = set(letters)
    result = set()
    for i in letters_set:
        for j in letters_set:
            for k in letters_set:
                for l in letters_set:
                    for m in letters_set:
                        palindrome = i + j + k + l + m + l + k + j + i
                        result.add(palindrome)
    return result