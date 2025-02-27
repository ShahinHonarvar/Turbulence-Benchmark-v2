import re

def palindrome_of_length_at_least_n(input_string, min_length=81):
    palindromes = set()
    string_pattern = re.compile('[a-zA-Z]+', re.I)
    words = string_pattern.findall(input_string)
    for word in words:
        word = word.lower()
        for i in range(len(word) - min_length + 1):
            for j in range(i + 1, min_length + i):
                if word[i:j + 1] == word[i:j + 1][::-1]:
                    palindromes.add(word[i:j + 1])
    return palindromes