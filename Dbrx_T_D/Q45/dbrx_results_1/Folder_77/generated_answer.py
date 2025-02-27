def palindromes_between_indices(s):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    letters_in_range = set(s[4:7].lower())
    palindromes = set()
    for i in range(4, 7):
        for j in range(i, 7):
            candidate = s[i] + s[i:i + j - i + 1][::-1] + s[j]
            if candidate in palindromes:
                continue
            if candidate and all((c in english_letters for c in candidate)):
                palindromes.add(candidate)
    return palindromes