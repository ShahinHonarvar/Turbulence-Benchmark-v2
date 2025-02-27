def palindromes_between_indices(s):
    s = s[4:9].lower()
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            for j in range(length // 2):
                if substring[j] != substring[length - j - 1]:
                    break
            else:
                palindrome = ''.join(substring)
                palindromes.add(palindrome)
    return palindromes