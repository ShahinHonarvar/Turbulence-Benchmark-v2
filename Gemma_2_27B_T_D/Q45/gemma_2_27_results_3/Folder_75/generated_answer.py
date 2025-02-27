def palindromes_between_indices(s):
    letters = s[2:5]
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                candidate = letter1 + letter2 + letter3
                if candidate == candidate[::-1] and len(candidate) >= 3:
                    palindromes.add(candidate.lower())
    return palindromes