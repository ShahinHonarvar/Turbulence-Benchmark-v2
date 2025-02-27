def palindromes_between_indices(input_string: str) -> set:
    palindromes = set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    letters_in_range = [char.lower() for char in input_string[3:10] if char.lower() in english_letters]
    for i in range(3, len(letters_in_range) + 1):
        for j in range(len(letters_in_range) - i + 1):
            palindrome = ''.join(letters_in_range[j:j + i])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes