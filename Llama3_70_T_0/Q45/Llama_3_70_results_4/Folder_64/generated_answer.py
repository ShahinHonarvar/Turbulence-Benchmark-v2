def palindromes_between_indices(s):
    s = s[4:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            for j in range(length // 2 + 1):
                for k in range(length // 2 + 1):
                    if substring[j] == substring[length - k - 1]:
                        palindrome = ''.join(substring[:j] + substring[length - k:])
                        if palindrome == palindrome[::-1]:
                            palindromes.add(palindrome)
    return palindromes