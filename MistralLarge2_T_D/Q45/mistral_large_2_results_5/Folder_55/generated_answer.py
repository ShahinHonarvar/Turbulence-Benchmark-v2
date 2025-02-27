def palindromes_between_indices(s):
    letters = {char.lower() for char in s[:3] if char.isalpha()}
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for j in range(i, i + length):
                palindrome = s[i:j + 1].lower()
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes