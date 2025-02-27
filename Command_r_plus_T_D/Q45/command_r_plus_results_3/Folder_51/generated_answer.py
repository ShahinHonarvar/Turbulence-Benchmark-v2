def palindromes_between_indices(s):
    letters = [c for c in s[3:6] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            sub_letters = letters[i:j]
            if len(sub_letters) >= 3 and sub_letters == sub_letters[::-1]:
                palindromes.add(''.join(sub_letters))
    return palindromes