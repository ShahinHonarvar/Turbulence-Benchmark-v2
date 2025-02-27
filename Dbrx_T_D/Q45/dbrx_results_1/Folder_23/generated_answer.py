import re

def palindromes_between_indices(input_string):
    input_string = input_string.lower()
    english_letters = re.findall('[a-z]', input_string[0:7])
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i, len(english_letters)):
            palindrome = ''.join(english_letters[i:j + 1])
            if palindrome == palindrome[::-1] and len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes