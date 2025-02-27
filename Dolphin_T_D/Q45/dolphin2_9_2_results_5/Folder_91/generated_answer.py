def palindromes_between_indices(s):
    letters = s[2:7].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            subs = letters[i:j]
            if subs == subs[::-1] and len(subs) >= 3:
                palindromes.add(subs)
    return palindromes