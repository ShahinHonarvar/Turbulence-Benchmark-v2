def palindromes_between_indices(s):
    s = s[4:10].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    if len(letters) < 2:
        return palindromes
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            sub = letters[i:i + length]
            for j in range(len(sub) // 2):
                if sub[j] != sub[-j - 1]:
                    break
            else:
                palindromes.add(''.join(sub))
    return palindromes