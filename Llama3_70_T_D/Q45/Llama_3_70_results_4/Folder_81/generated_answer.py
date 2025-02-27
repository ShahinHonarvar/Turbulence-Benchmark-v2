def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for j in range(i + length - 1, i - 1, -1):
                sub = letters[i:j + 1]
                sub += sub[:length // 2][::-1]
                if length % 2 == 0:
                    sub += sub[length // 2:][::-1]
                palindromes.add(''.join(sub))
    return palindromes