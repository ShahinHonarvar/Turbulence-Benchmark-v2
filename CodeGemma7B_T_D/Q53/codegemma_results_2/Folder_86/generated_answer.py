def palindrome_of_length_at_least_n(s):
    """Finds all palindromes of length greater than or equal to n in a string."""
    words = s.split()
    letters = list(s)
    palindromes = []
    for word in words:
        if word == word[::-1]:
            if len(word) >= n:
                palindromes.append(word)
    for i in range(len(letters)):
        if letters[i] == letters[i + 1]:
            palindrome = letters[i] + letters[i + 1]
            if len(palindrome) >= n:
                palindromes.append(palindrome)
    for i in range(len(letters)):
        if letters[i] == letters[i + 1] == letters[i + 2]:
            palindrome = letters[i] + letters[i + 1] + letters[i + 2]
            if len(palindrome) >= n:
                palindromes.append(palindrome)
    return set(palindromes)