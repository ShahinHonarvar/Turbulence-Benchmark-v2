def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            for j in range(length // 2 + 1):
                palindrome = substring[:j] + substring[j:j + length - 2 * j] + substring[j + length - 2 * j:][::-1]
                palindromes.add(''.join(palindrome))
    return palindromes