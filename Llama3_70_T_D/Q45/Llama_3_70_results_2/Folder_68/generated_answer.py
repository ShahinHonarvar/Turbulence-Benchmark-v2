def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:9] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            sub = letters[i:i + length]
            for j in range(length):
                if length % 2 == 0 or j != length // 2:
                    if sub[j] != sub[length - j - 1]:
                        break
            else:
                palindromes.add(''.join(sub))
    return palindromes