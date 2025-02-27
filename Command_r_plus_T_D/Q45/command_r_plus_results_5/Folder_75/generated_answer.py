def palindromes_between_indices(input_string: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters_in_range = set((char for char in input_string[2:5] if char in english_letters))
    for letter1 in letters_in_range:
        for letter2 in letters_in_range:
            for letter3 in letters_in_range:
                palindrome = letter1 + letter2 + letter3
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes