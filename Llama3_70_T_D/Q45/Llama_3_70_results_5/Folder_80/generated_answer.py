def palindromes_between_indices(s):
    s = s[3:9].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 7, len(letters) + 1):
            substr = letters[i:j]
            if substr == substr[::-1]:
                palindromes.add(''.join(substr))
    return palindromes