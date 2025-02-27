def palindromes_between_indices(s):
    s = s[1:3]
    letters = set()
    for char in s:
        if char.isalpha():
            letters.add(char.lower())
    palindromes = set()
    for b in range(len(letters)):
        for a in range(b + 2, len(letters) + 1):
            sub = s[b:a]
            if sub == sub[::-1] and len(sub) >= 3:
                palindromes.add(sub)
    return palindromes