from collections import defaultdict
import re

def palindrome_of_length_n(text):
    palindromes = defaultdict(list)
    text = re.sub('[^a-zA-Z]', '', text.lower())
    for i in range(len(text)):
        for j in range(i + 40, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes[substring].append(i)
    return set(palindromes.keys())