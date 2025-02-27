def palindromes_between_indices(s):
    s = s[8:10].lower()
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 2:
        return set()
    if len(letters) == 2 and letters[0] == letters[1]:
        return {letters[0] * 2, letters[0] * 3}
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for j in range(i + length - 1, len(letters)):
                substring = letters[i:j + 1]
                if substring == substring[::-1]:
                    palindrome = ''.join(substring)
                    if len(palindrome) >= 3:
                        palindromes.add(palindrome)
    return palindromes