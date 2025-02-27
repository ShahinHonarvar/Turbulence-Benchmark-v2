from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    char_frequency = defaultdict(int)
    for char in text:
        char_frequency[char] += 1
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes