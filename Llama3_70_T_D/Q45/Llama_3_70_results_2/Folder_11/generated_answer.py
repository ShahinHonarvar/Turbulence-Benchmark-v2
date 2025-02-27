def palindromes_between_indices(s):
    s = s[3:8].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            for j in range(length // 2):
                if substring[j] != substring[length - j - 1]:
                    break
            else:
                palindrome = ''.join(substring)
                if all((palindrome.count(c) >= 2 for c in set(palindrome))):
                    palindromes.add(palindrome)
    return palindromes