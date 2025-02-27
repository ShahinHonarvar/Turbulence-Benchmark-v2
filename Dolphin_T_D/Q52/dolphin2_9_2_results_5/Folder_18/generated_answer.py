import re

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 391):
        sub_string = string[i:i + 392]
        sub_string_lower = sub_string.lower()
        english_sub_string = re.findall('[a-zA-Z]', sub_string_lower)
        if english_sub_string == english_sub_string[::-1]:
            palindromes.add(sub_string)
    return palindromes