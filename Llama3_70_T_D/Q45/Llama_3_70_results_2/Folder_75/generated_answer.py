def palindromes_between_indices(s):
    letters = set((s[i].lower() for i in range(2, 5) if s[i].isalpha()))
    all_palindromes = set()
    for length in range(3, len(letters) + 1):
        for palindrome in generate_palindromes(letters, length):
            all_palindromes.add(palindrome)
    return all_palindromes

def generate_palindromes(letters, length):
    if length == 0:
        return {''}
    elif length == 1:
        return letters
    else:
        palindromes = set()
        for letter in letters:
            for other_palindrome in generate_palindromes(letters, length - 2):
                palindromes.add(letter + other_palindrome + letter)
        return palindromes