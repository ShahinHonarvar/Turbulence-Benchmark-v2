def palindromes_between_indices(s):
    letters = [char for char in s[3:5] if char.isalpha()]
    letters = [char.lower() for char in letters]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i] + letters[j] + letters[i]
            palindromes.add(palindrome)
    return palindromes