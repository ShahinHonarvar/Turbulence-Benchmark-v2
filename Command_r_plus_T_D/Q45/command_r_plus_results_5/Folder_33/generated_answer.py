def palindromes_between_indices(input_string: str) -> set:
    palindromes = set()
    english_letters = ''
    for char in input_string[7:10]:
        if char.isalpha():
            english_letters += char.lower()
    for i in range(len(english_letters)):
        for j in range(i + 3, len(english_letters) + 1):
            palindrome = english_letters[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes