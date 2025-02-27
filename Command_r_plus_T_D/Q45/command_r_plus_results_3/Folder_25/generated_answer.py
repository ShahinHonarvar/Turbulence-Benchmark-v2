def palindromes_between_indices(input_string: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    sub_string = input_string[1:5].lower()
    for letter in sub_string:
        if letter in english_letters:
            english_letters.remove(letter)
    for letter in english_letters:
        palindrome = letter + sub_string + letter
        if is_palindrome(palindrome):
            palindromes.add(palindrome)
    return palindromes