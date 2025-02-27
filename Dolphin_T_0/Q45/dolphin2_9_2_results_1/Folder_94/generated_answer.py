def palindromes_between_indices(s):
    letters = s[3] + s[4] + s[3].lower() + s[4].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            sub = ''.join(sorted(letters[i:j]))
            if sub == sub[::-1] and len(sub) >= 3:
                palindromes.add(sub)
    return palindromes if palindromes else '{}'