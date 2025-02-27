def palindromes_between_indices(s):
    s = s[3:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            for j in range(length // 2 + 1):
                if substring[j] != substring[length - j - 1]:
                    break
            else:
                palindrome = ''.join(substring)
                palindromes.add(palindrome)
    return palindromes