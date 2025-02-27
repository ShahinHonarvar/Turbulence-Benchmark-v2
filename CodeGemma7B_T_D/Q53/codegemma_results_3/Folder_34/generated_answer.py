import re

def palindrome_of_length_at_least_n(word):
    palindromes = set()
    for i in range(len(word)):
        for j in range(i + 68, len(word)):
            substring = word[i:j + 1]
            if substring == substring[::-1]:
                strip_letters = re.sub('[^a-zA-Z]', '', substring)
                if len(strip_letters) == len(substring):
                    palindromes.add(substring.lower())
    return palindromes