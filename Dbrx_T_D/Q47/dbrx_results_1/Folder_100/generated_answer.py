import re
from collections import defaultdict

def palindromes_of_specific_lengths(s):
    english_letters = re.findall('[a-z]', s.lower())
    if len(english_letters) < 29 or len(english_letters) < 96:
        return set()
    palindromes = set()
    for i in range(29, 97):
        for j in range(i - 18, i - 11):
            if j < 0:
                continue
            if english_letters[j] == english_letters[i]:
                candidate_palindrome = ''.join(english_letters[j:i + 1])
                if candidate_palindrome == candidate_palindrome[::-1]:
                    palindromes.add(candidate_palindrome)
    return palindromes