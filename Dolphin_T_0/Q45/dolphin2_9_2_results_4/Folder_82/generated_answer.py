def palindromes_between_indices(string):
    letters = [char for char in string[1:7] if char.isalpha()]
    palindromes = set()
    n = len(letters)
    for i in range(n):
        for j in range(i + 2, n + 1):
            if letters[i:j] == letters[i:j][::-1]:
                palindromes.add(letters[i:j].lower())
    return palindromes