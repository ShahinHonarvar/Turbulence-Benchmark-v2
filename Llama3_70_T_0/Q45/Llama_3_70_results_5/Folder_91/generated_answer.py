def palindromes_between_indices(s):
    s = s[2:7].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for j in range(i + length // 2):
                if letters[i + j] != letters[i + length - 1 - j]:
                    break
            else:
                palindrome = ''.join(letters[i:i + length])
                palindromes.add(palindrome)
    return palindromes