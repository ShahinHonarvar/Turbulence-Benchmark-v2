def palindromes_between_indices(input_string: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    input_string = input_string.lower()
    subset = set(input_string[4:10])
    palindromes = set()
    for letter in english_letters:
        if letter in subset:
            subset.remove(letter)
    for palindrome_length in range(6, len(subset) + 1):
        for arrangement in permutations(subset, palindrome_length):
            word = ''.join(arrangement)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes