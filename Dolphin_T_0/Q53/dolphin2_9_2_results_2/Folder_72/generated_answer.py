import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    palindromes = set()
    for i in range(88, 0, -1):
        for j in range(len(string) - i + 1):
            sub_string = string[j:j + i]
            if sub_string == sub_string.lower():
                if sub_string == sub_string[::-1]:
                    palindromes.add(sub_string)
    return palindromes