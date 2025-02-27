def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:10] if c.isalpha()]
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            for j in range(length // 2):
                if substring[j] != substring[length - j - 1]:
                    break
            else:
                palindrome = ''.join(substring)
                rev = palindrome[::-1]
                if palindrome == rev:
                    palindromes.add(palindrome)
    return palindromes