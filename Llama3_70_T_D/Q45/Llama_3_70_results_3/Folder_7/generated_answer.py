def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:10] if c.isalpha()]
    palindromes = set()
    for length in range(7, 10):
        if len(letters) < length:
            break
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            for j in range(length // 2 + 1):
                if substring[j] != substring[length - j - 1]:
                    break
            else:
                palindrome = ''.join(substring)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes