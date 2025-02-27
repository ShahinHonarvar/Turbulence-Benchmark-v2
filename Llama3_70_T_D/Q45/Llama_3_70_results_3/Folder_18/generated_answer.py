def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 2:
        return set()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substr = letters[i:i + length]
            for j in range(length // 2 + 1):
                palindrome = substr[:j] + substr[j:j + 1] * 2 + substr[j + 1:length - j]
                if palindrome == palindrome[::-1]:
                    palindromes.add(''.join(palindrome))
    return palindromes