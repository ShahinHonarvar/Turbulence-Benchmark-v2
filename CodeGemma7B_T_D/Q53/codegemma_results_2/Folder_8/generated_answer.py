import re
from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    """
    Return the set of palindromes of the length greater or equal to 45.
    """
    text = re.sub('[^A-Za-z]', '', text)
    text = text.lower()
    letter_counts = defaultdict(int)
    for char in text:
        letter_counts[char] += 1
    palindromes = set()
    for char in letter_counts:
        for count in range(letter_counts[char]):
            if count < 45 - 1:
                continue
            palindrome = []
            i = 0
            while i < count:
                palindrome.append(char)
                i += 1
            j = 0
            while j < len(palindrome):
                palindrome.insert(0, char)
                j += 1
            palindromes.add(''.join(palindrome))
    return palindromes