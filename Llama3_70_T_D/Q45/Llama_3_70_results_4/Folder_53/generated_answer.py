def palindromes_between_indices(string):
    substring = string[4:9].lower()
    letters = [char for char in substring if char.isalpha()]
    letters_set = set(letters)
    if len(letters_set) < 3:
        return set()
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for palindrome in generate_palindromes(letters_set, length):
            palindromes.add(palindrome)
    return palindromes

def generate_palindromes(letters, length):
    if length == 1:
        for letter in letters:
            yield letter
    elif length == 2:
        for letter1 in letters:
            for letter2 in letters:
                yield (letter1 + letter2)
    else:
        for letter1 in letters:
            for letter2 in letters:
                for middle in generate_palindromes(letters, length - 2):
                    if len(middle) >= length - 2:
                        yield (letter1 + letter2 + middle + letter2 + letter1)