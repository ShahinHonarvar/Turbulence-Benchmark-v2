def palindromes_between_indices(input_string: str) -> set:
    palindromes = set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    sub_string = input_string[6:9].lower()
    for letter in sub_string:
        if letter in english_letters:
            palindrome = sub_string.count(letter) >= 2
            if palindrome:
                palindromes.add(sub_string)
                break
    return palindromes