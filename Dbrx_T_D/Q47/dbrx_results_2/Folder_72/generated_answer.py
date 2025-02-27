import re

def palindromes_of_specific_lengths(s):
    english_letters_only = re.findall('[a-zA-Z]', s)
    substr = ''.join(english_letters_only[26:91])
    palindrome_set = set()
    for length in range(27, 59):
        for i in range(len(substr) - length + 1):
            if substr[i:i + length].lower() == substr[i:i + length][::-1].lower():
                palindrome_set.add(substr[i:i + length])
    return palindrome_set