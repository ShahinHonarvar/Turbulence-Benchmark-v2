def palindromes_between_indices(s):
    letters = set((s[i].lower() for i in range(1, 7) if s[i].isalpha()))
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for palindrome in generate_palindromes(letters, length):
            palindromes.add(palindrome)
    return palindromes

def generate_palindromes(letters, length):
    if length == 0:
        yield ''
    elif length == 1:
        for letter in letters:
            yield letter
    else:
        for letter in letters:
            letters_copy = letters.copy()
            letters_copy.remove(letter)
            for left in generate_palindromes(letters_copy, length - 2):
                yield (letter + left + letter)