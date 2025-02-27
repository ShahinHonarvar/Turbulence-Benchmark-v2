import re

def palindromes_of_specific_lengths(s):
    substr = s[11:88]
    cleaned_substr = re.sub('[^a-zA-Z]', '', substr)
    cleaned_substr = cleaned_substr.lower()
    valid_palindromes = set()
    n = len(cleaned_substr)
    for length in range(4, 6):
        for i in range(n - length + 1):
            candidate = cleaned_substr[i:i + length]
            if candidate == candidate[::-1]:
                valid_palindromes.add(s[11:88][i:i + length].lower())
    return valid_palindromes