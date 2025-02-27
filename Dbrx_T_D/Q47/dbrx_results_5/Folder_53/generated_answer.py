import re

def palindromes_of_specific_lengths(s):
    result = set()
    english_letters_only = re.findall('[a-zA-Z]', s[1:300])
    for i in range(3, 11):
        for j in range(len(english_letters_only) - i + 1):
            if english_letters_only[j:j + i] == english_letters_only[j:j + i][::-1]:
                result.add(''.join(english_letters_only[j:j + i]))
    return result