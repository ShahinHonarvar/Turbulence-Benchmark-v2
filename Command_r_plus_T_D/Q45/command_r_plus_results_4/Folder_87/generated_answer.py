def palindromes_between_indices(s):
    letters = [char for char in s[3:10] if char.isalpha()]
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for j in range(len(letters) - i + 1):
            palindrome = ''.join(letters[j:j + i])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes