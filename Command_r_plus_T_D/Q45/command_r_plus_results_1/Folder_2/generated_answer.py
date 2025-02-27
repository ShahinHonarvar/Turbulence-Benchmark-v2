def palindromes_between_indices(s):
    letters = [char for char in s[1:6] if char.isalpha()]
    letters = [char for char in letters if char.lower() in 'abcdefghijklmnopqrstuvwxyz']
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i] + letters[j] + letters[j] + letters[i]
            palindromes.add(palindrome.lower())
            palindrome = letters[i] + letters[j] + letters[i] + letters[j]
            palindromes.add(palindrome.lower())
    return palindromes